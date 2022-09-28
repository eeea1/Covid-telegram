import telegram
import json
import os
Token = os.environ['TOKEN']
Chat_Id = os.environ['CHAT_ID']
bot = telegram.Bot(token=Token)
chat_id = Chat_Id
result = ""
with open('./result.json') as file:
    contents = file.read()
    load_data = json.loads(contents)
#
def switch(key):
  load_data.get(key)

for key ,value in load_data.items():
    new_key = switch(key)
    if new_key != '-':
        result += f'- {key}: {value}명\n'
bot.sendMessage(chat_id=chat_id, text=result)
