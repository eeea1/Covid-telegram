from bs4 import BeautifulSoup
import requests
import json
import os

Servicekey = os.environ['SERVICEKEY']
avl = {}
url = 'http://apis.data.go.kr/1352000/ODMS_COVID_02/callCovid02Api'
params ={'serviceKey' : Servicekey, 'pageNo' : '1', 'numOfRows' : '500', 'apiType' : 'xml', 'status_dt' : '20220906' }
response =requests.get(url, params=params) #url
html = response.text #url을 해석하기 쉽게 텍스트형태로 전환.
soup = BeautifulSoup(html, 'html.parser') #bs4를 토토sp = soup.find('item').get_text()
b = (sp.split('\n'))
j = 0
for i in range(1,12):
    j += i # 1,3,5,7...
    tt = soup.item.contents[j]
    avl[tt.name] = b[i]
    j = i
with open('./result.json', 'w') as file:
    json.dump(avl, file)
with open('./result.json') as file:
    contents = file.read()
    load_data = json.loads(contents)
print(load_data)
