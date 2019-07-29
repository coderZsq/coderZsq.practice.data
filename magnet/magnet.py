# coding=utf-8

from flask import Flask
from lxml import etree
import cfscrape
import json
import filter
from selenium import webdriver
import time
import datetime
import re

app = Flask(__name__)

def baidu():
	driver = webdriver.Chrome()
	querys = []
	for query in querys:
		print ("fetch - " + query)
		driver.get("https://www.baidu.com/s?wd=" + query + " 百度百科")
		content = driver.page_source
		dom = etree.HTML(content)
		url = dom.xpath("//div[@id='content_left']//h3/a/@href")[0]
		driver.get(url)
		content = driver.page_source
		dom = etree.HTML(content)
		infonames = []
		infonames = dom.xpath("//dt[contains(@class, 'basicInfo-item') and contains(@class, 'name')]//text()")
		infovalues = []
		for infovalue in dom.xpath("//dd[contains(@class, 'basicInfo-item') and contains(@class, 'value')]//text()"):
			infovalues.append(infovalue.replace('\n', ''))
		para = re.sub(r'\[\d+\]', '', ''.join(dom.xpath("//div[@class='para']//text()")).replace('参考资料', '').replace('\n', '').replace('.', ''))
		item = {}
		item["names"] = infonames
		item["values"] = infovalues
		item["para"] = para
		dumps = json.dumps(item, indent=4)
		with open('./data/baidu/bd_' + query + '.json', 'w') as f:
			f.write(dumps)
	driver.quit()

def beiwo():
	driver = webdriver.Chrome()
	querys = []
	domain = "http://www.beiwo888.com"
	for query in querys:
		print(query)
		driver.get(domain + "/index.php?s=vod-search&typeid=2&wd=" + query)
		content = driver.page_source
		dom = etree.HTML(content)
		urls = dom.xpath("//a[@class='play-img']/@href")
		names = []
		if len(urls) > 0:
			driver.get(domain + urls[0])
			content = driver.page_source
			dom = etree.HTML(content)
			names = dom.xpath("//div[@class='downlist']//p[@class='dwon_xl']//text()")
			actions = dom.xpath("//div[@class='downlist']//p[@class='dwon_xl']/a/@href")
			result = []
			for i in range(len(actions)):
				item = {}
				item["name"] = names[i]
				item["action"] = actions[i]
				result.append(item)
			item = {}
			item[query] = result
			dumps = json.dumps(item, indent=4)
			with open('./data/beiwo/bw_' + query + '.json', 'w') as f:
				f.write(dumps)
	driver.quit()

def piaohua():
	driver = webdriver.Chrome()
	querys = []
	domain = "https://www.piaohua.com"
	for query in querys:
		print (query)
		driver.get(domain + "/plus/search.php?kwtype=0&keyword=" + query + "&searchtype=%E5%BD%B1%E8%A7%86%E6%90%9C%E7%B4%A2")
		content = driver.page_source
		dom = etree.HTML(content)
		urls = dom.xpath("//div[@class='txt']//a/@href")
		names = []
		if len(urls) > 0:
			driver.get(domain + urls[0])
			content = driver.page_source
			dom = etree.HTML(content)
			name = dom.xpath("//h1/text()")[0]
			print(name)
			actions = dom.xpath("//div[@class='bot']//a//text()")
			if len(actions) > 1:
				del actions[0]
			print(actions)
			result = []
			for i in range(len(actions)):
				item = {}
				item["name"] = str(i) + "-" + name
				item["action"] = actions[i]
				result.append(item)
			item = {}
			item[query] = result
			dumps = json.dumps(item, indent=4)
			with open('./data/piaohua/ph_' + query + '.json', 'w') as f:
				f.write(dumps)
		time.sleep(2)
	driver.quit()


def thunder():
	driver = webdriver.Chrome()
	querys = []
	domain = "https://www.22tu.cc"
	for query in querys:
		print (query)
		driver.get(domain + "/vodsearch/" + query +"-------------/")
		content = driver.page_source
		dom = etree.HTML(content)
		urls = dom.xpath("//ul[@class='mlist']//a/@href")
		if len(urls) > 0:
			driver.get(domain + urls[0])
			content = driver.page_source
			dom = etree.HTML(content)
			names = dom.xpath("//div[@class='endpage']//span[@class='down-title']/a//text()")
			actions = dom.xpath("//div[@class='endpage']//span[@class='down-title']/a/@href")
			result = []
			for i in range(len(actions)):
				item = {}
				item["name"] = names[i]
				item["action"] = actions[i]
				result.append(item)
			item = {}
			item[query] = result
			dumps = json.dumps(item, indent=4)
			with open('./data/thunder/th_' + query + '.json', 'w') as f:
				f.write(dumps)
		time.sleep(3)
	driver.quit()

def generate():
	gfw = filter.DFAFilter()
	gfw.parse("keywords")
	driver = webdriver.Chrome()
	querys = []
	print(len(querys))
	domain = "http://zhongzishenqiso.com"
	for query in querys:
		print (query)
		driver.get(domain + "/shenqi/" + query + "/1-0-0/")
		content = driver.page_source
		html = content.replace("<b>", "")
		dom = etree.HTML(html)
		names = dom.xpath("//dl[@class='item']/dt/a//text()")
		urls = dom.xpath("//dl[@class='item']/dt/a/@href")
		actions = []
		for url in urls:
			driver.get(domain + url)
			content = driver.page_source
			dom = etree.HTML(content)
			action = dom.xpath("//p[contains(@class, 'dd') and contains(@class, 'magnet')]/a/@href")
			if len(action) > 0:
				actions.append(action[0])
		for i in range(len(names)):
			name = names[i]
			names[i] = gfw.filter(name, " ")
		result = []
		for i in range(len(actions)):
			item = {}
			item["name"] = names[i]
			item["action"] = actions[i]
			result.append(item)
		item = {}
		item[query] = result
		dumps = json.dumps(item, indent=4)
		with open('../data/magnet/' + query + '.json', 'w') as f:
			f.write(dumps)
	driver.quit()
	return "done"

# @app.route('/baike/<query>')
def baike(query):
	result = []
	try:
		with open('./data/baidu/bd_' + query + '.json', 'r') as f:
			data = json.load(f)
			result.append(data)
	except IOError:
		print (path + "file is not accessible.")
	return {"data":result}

@app.route('/fetch/<query>/<env>')
def fetch(query, env):
	print ("fetch - " + query)

	if env == "release":
		with open('./fetchs/' + datetime.datetime.now().strftime('%Y-%m-%d') + '.txt', 'a+') as f:
			f.write('"' + query + '", ' + '\n')

	result = []
	for path in ['./data/thunder/th_', './data/piaohua/ph_', './data/beiwo/bw_', './data/magnet/']:
		try:
			with open(path + query + '.json', 'r') as f:
				data = json.load(f)
				result.extend(data[query])
		except IOError:
			print (path + "file is not accessible.")
	if len(result) > 0:
		return {"data":result}
	
	if env == "release":
		with open('./querys/' + datetime.datetime.now().strftime('%Y-%m-%d') + '.txt', 'a+') as f:
			f.write('"' + query + '", ' + '\n')

	gfw = filter.DFAFilter()
	gfw.parse("keywords")

	scraper = cfscrape.create_scraper()
	content = scraper.get("https://www.torrentkitty.tv/search/" + query).content
	html = content.decode('ISO-8859-1').encode('ISO-8859-1').decode('utf8')
	dom = etree.HTML(html)
	# with open(query+'.html', "w", encoding="utf-8") as f:
	# 	f.write(etree.tostring(html, encoding="utf-8").decode())
	names = dom.xpath("//table[@id='archiveResult']//td[@class='name']//text()")
	actions = dom.xpath("//table[@id='archiveResult']//td[@class='action']/a[2]/@href");
	for i in range(len(names)):
		name = names[i]
		names[i] = gfw.filter(name, " ")

	result = []
	for i in range(len(actions)):
		item = {}
		item["name"] = names[i]
		item["action"] = actions[i]
		result.append(item)
	return {"data":result}

# @app.route('/tags/<type>')
def tag(type):
	url = "https://movie.douban.com/j/search_tags?type=" + type + "&source=index"
	scraper = cfscrape.create_scraper()
	result = json.loads(scraper.get(url).content)["tags"]
	return {"data":result}

# @app.route('/<type>/<tag>/<page_start>')
def movie(type, tag, page_start):
	url = "https://movie.douban.com/j/search_subjects?type=" + type +"&tag=" + tag + "&sort=recommend&page_limit=20&page_start=" + page_start
	scraper = cfscrape.create_scraper()
	subjects = json.loads(scraper.get(url).content)["subjects"]
	result = []
	for i in range(len(subjects)):
		item = {}
		item["title"] = subjects[i]["title"]
		item["img"] = subjects[i]["cover"]
		item["rate"] = subjects[i]["rate"]
		result.append(item)
	return {"data":result}

# @app.route('/chart')
def chart():
	scraper = cfscrape.create_scraper()
	content = scraper.get("https://movie.douban.com/chart").content
	html = content.decode()
	dom = etree.HTML(html)
	titles = dom.xpath("//a[@class='nbg']/@title")
	imgs = dom.xpath("//a[@class='nbg']/img/@src")
	rates = dom.xpath("//span[@class='rating_nums']/text()")
	result = []
	for i in range(len(titles)):
		item = {}
		item["title"] = titles[i]
		item["img"] = imgs[i]
		item["rate"] = rates[i]
		result.append(item)
	return {"data":result}

# @app.route('/top250/<start>')
def top250(start):
	scraper = cfscrape.create_scraper()
	content = scraper.get("https://movie.douban.com/top250?start=" + start).content
	html = content.decode()
	dom = etree.HTML(html)
	titles = dom.xpath("//ol[@class='grid_view']//div[@class='pic']//img/@alt")
	imgs = dom.xpath("//ol[@class='grid_view']//div[@class='pic']//img/@src")
	rates = dom.xpath("//ol[@class='grid_view']//span[@class='rating_num']//text()")
	quotes = dom.xpath("//ol[@class='grid_view']//span[@class='inq']//text()")
	result = []
	for i in range(len(titles)):
		item = {}
		item["title"] = titles[i]
		item["img"] = imgs[i]
		item["rate"] = rates[i]
		item["quote"] = quotes[i]
		result.append(item)
	return {"data":result}

if __name__ == '__main__':
	app.run()
	# thunder()
	# piaohua()
	# beiwo()
	# generate()
	# baidu()