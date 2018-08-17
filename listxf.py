from lxml import etree
import requests
import time
'''
获取home前5页的全部房源信息
'''

url = 'http://xf.m.pinganfang.com/sh'
# requests.get()返回的是URL的响应码200，
# 加上.text，下载的是网页的源码
data = requests.get(url,verify=False).text

# 使用etree.HTML()方法解析data数据
# s = etree.HTML(data)
# xfname = s.xpath('//*[@id="listWrap"]/ul/li/a/div[2]/div/h3/em/text()')
# for name in xfname:
# 	time.sleep(0.2)
# 	print(name)
count = 0
s = etree.HTML(data)
file = s.xpath('//*[@id="listWrap"]/ul/li/a/div[2]/div')
for i in file: 
	name = i.xpath('./h3/em/text()')[count]
	price = i.xpath('div[3]/text()')[count]
	adds = i.xpath('div[1]/text()')[count].strip('\\')
	# count += 1
	time.sleep(0.2)
	# print(name)
	# print("%s,%s"%(name,adds))
	print('{} -- {} -- {}'.format(name,price,adds))
# print(count)

# //*[@id="listWrap"]/ul/li[2]/a/div[2]/div/div[3]
# //*[@id="listWrap"]/ul/li[4]/a/div[2]/div/h3/em
# //*[@id="listWrap"]/ul/li[4]/a/div[2]/div/div[1]
# //*[@id="listWrap"]/ul/li[4]/a/div[2]/div/div[2]






