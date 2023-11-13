import config
import prompt

import pinecone
from langchain.vectorstores import Pinecone
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, LLMRequestsChain
from langchain.tools import Tool
from langchain.agents import AgentType, initialize_agent


class Util:
    def __init__(self):
        super(Util, self).__init__()
        self.configs = config.ConfigParser()

        self.ChatOpenAI = ChatOpenAI(
            openai_api_key=self.configs.get(key='openai')['api_key'],
            model_name=self.configs.get(key='openai')['chat_model'],
            temperature=0, max_tokens=2048,
        )

        self.EmbeddingOpenAI = OpenAIEmbeddings(
            openai_api_key=self.configs.get(key='openai')['api_key'],
            model=self.configs.get(key='openai')['embedding_model'],
        )

        pinecone.init(
            api_key=self.configs.get(key='pinecone')['api_key'],
            environment=self.configs.get(key='pinecone')['environment'],
        )
        self.VDBPineconeIndex = Pinecone.get_pinecone_index(self.configs.get(key='pinecone')['index'])

    # 利用大语言模型自身知识
    def generic_func(self, query):
        generic_prompt = PromptTemplate(
            input_variables=['query'],
            template=prompt.GENERIC_CHAIN_PROMPT
        )
        llm_chain = LLMChain(llm=self.ChatOpenAI, prompt=generic_prompt)
        return llm_chain.run(query)

    # 利用搜索引擎的查询功能
    def request_func(self, query):
        request_prompt = PromptTemplate(
            input_variables=['query', 'requests_result'],
            template=prompt.REQUEST_CHAIN_TEMPLATE
        )
        # 根据搜索引擎获取回来后的数据结合本身问题再加工
        llm_chain = LLMChain(llm=self.ChatOpenAI, prompt=request_prompt, verbose=True)
        # 根据用户提供的问题及网站进行搜索
        request_chain = LLMRequestsChain(llm_chain=llm_chain, verbose=True)

        # 因为浏览器中的地址不允许有空，所以使用+进行替换
        inputs = {
            "query": query,
            "url": "https://www.google.com/search?q=" + query.replace(' ', '+')
        }
        return request_chain.run(inputs)

    # 利用已经存在的业务数据库提供问题咨询
    def database_func(self, query):
        # 数据库连接
        connection = f"mysql+pymysql://{self.configs.get(key='mysql')['user']}:" \
                     f"{self.configs.get(key='mysql')['password']}@" \
                     f"{self.configs.get(key='mysql')['host']}/" \
                     f"{self.configs.get(key='mysql')['database']}"
        # 数据库对象实例化
        database = SQLDatabase.from_uri(connection)
        db_chain = SQLDatabaseChain(llm=self.ChatOpenAI, database=database, verbose=True)
        return db_chain.run(query)

    # 利用向量数据库中的私有知识库提供问题解答
    def retrival_func(self, query):
        # 问题向量化
        vector = self.EmbeddingOpenAI.embed_query(query)
        # 相似度搜索
        documents = self.VDBPineconeIndex.query(
            top_k=3,
            include_values=False,
            include_metadata=True,
            vector=vector
        )
        # 抑制不相似的问题
        retrival = ""
        for doc in documents['matches']:
            if float(doc["score"]) > 0.75:
                retrival += f'问题:{doc["metadata"]["question"]} 答案:{doc["metadata"]["answer"]}\n'
        # 根据相似度搜索回来后的数据结合本身问题再加工
        request_prompt = PromptTemplate(
            input_variables=['query', 'requests_result'],
            template=prompt.RETRIVAL_CHAIN_TEMPLATE
        )
        llm_chain = LLMChain(llm=self.ChatOpenAI, prompt=request_prompt, verbose=True)
        inputs = {
            "query": query,
            "requests_result": retrival
        }
        return llm_chain.run(inputs)

    # 实例化 Agent 对象
    def initialize_agent(self):
        # 工具集定义
        tools = [
            Tool.from_function(
                func=self.generic_func,
                name="大语言模型查询",
                description="可以解答通用领域的知识"
            ),
            Tool.from_function(
                func=self.database_func,
                name="员工信息查询",
                description="可以帮助用户解答员工的问题"
            ),
            Tool.from_function(
                func=self.request_func,
                name="时效性问题查询",
                description="可以帮助用户查询具有时效性问题"
            ),
            Tool.from_function(
                func=self.retrival_func,
                name="墨问西东知识查询",
                description="可以帮助用户有关墨问西东的知识"
            ),
        ]

        # 赋予使用工具的能力
        agent = initialize_agent(
            tools=tools,
            llm=self.ChatOpenAI,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True
        )

        return agent
