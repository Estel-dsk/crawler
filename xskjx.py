import requests
from lxml import etree

url = 'https://movie.douban.com/subject/1292052/'
# 下载网页信息，并且转换为文本
data = requests.get(url).text
s = etree.HTML(data)

# 使用text()方法，取得xpath的文本信息
film = s.xpath('//*[@id="content"]/h1/span[1]/text()')
score = s.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
print("电影名称：",film)
print("电影评分：",score)