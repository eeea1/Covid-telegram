import json
import os
import requests
from bs4 import BeautifulSoup

apikey = os.environ['SERVICEKEY'] # API 키를 다음 란에 입력해 주세요.
korea = "https://api.corona-19.kr/korea/beta/?serviceKey="
response = requests.get(korea + apikey)
message = response.text



# 크롤링 방법 1: BeautifulSoup 활용하기
soup = BeautifulSoup(message, 'html.parser') # parser 종류는 xml, html 선택 가능
sp = soup
result = eval(sp.get_text())["korea"]
with open('./result.json', 'w') as file:
    json.dump(result, file)
with open('./result.json') as file:
    contents = file.read()
    load_data = json.loads(contents)
print(load_data)
