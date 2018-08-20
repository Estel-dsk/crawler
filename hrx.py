from lxml import etree
import requests
import time

for m in range(3):
	url = 'http://xf.m.st.anhouse.com.cn/sh/api/lp/list?page={}&pageSize=15'.format(m)
	data = requests.get(url,verify=False).json()
	time.sleep(0.2)
	for i in range(15):
		lpname = data['data']['data']['list'][i]['title']
		price = data['data']['data']['list'][i]['unitPrice']
		time.sleep(0.2)
		print("{}--{}".format(lpname,price))








# print(data['data']['data']['list'][1]['title'])
