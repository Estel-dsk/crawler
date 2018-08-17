
from lxml import etree #解析模块
import requests #请求模块
import time

for a in range(10):
	# print(a)
	url = 'https://book.douban.com/top250?start={}'.format(a*25)
	data = requests.get(url).text

	s = etree.HTML(data)
	file = s.xpath('//*[@id="content"]/div/div[1]/div/table')

	for div in file:
		bname = div.xpath('./tr/td[2]/div[1]/a/@title')
		score = div.xpath('./tr/td[2]/div[2]/span[2]/text()')
		time.sleep(0.2)
		print("{} {}".format(bname,score))




