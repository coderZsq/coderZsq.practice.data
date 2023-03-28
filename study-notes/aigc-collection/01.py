import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

COMPLETION_MODEL = "text-davinci-003"

# prompt = """
# Consideration proudct : 工厂现货PVC充气青蛙夜市地摊热卖充气玩具发光蛙儿童水上玩具

# 1. Compose human readable product title used on Amazon in english within 20 words.
# 2. Write 5 selling points for the products in Amazon.
# 3. Evaluate a price range for this product in U.S.

# Output the result in json format with three properties called title, selling_points and price_range
# """

# {
#     "title": "Glow-in-the-Dark Inflatable PVC Frog Night Market Hot Selling Water Toy for Kids",
#     "selling_points": [
#         "Made of durable PVC material",
#         "Glow-in-the-dark design for night play",
#         "Inflatable design for easy storage and transport",
#         "Fun water toy for kids of all ages",
#         "Comes with a repair patch for convenience"
#     ],
#     "price_range": "$10 - $20"
# }

prompt = """
Man Utd must win trophies, says Ten Hag ahead of League Cup final

请将上面这句话的人名提取出来，并用json的方式展示出来
"""

# {
#   "names": ["Ten Hag"]
# }

def get_response(prompt):
    completions = openai.Completion.create(
        engine=COMPLETION_MODEL,
        prompt=prompt,
        max_tokens=512,
        n=1,
        stop=None,
        temperature=0.0,
    )
    message = completions.choices[0].text
    return message

print(get_response(prompt))