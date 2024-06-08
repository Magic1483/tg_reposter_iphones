import pyrogram
from pyrogram import Client,filters
from pyrogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,InlineKeyboardButton)
import toml
from datetime import datetime
import json
import re


today = datetime.today()
formatted_date = today.strftime("%d/%m/%Y")

CONFIG = toml.load('CONFIG.toml')

api_id=CONFIG['api_id']
api_hash =CONFIG['api_hash']

app = Client("userbot",api_id=api_id,api_hash=api_hash)

# @app.on_message(filters.private)
# async def hello(client, message):
#     await message.reply("Hello from Pyrogram-Dev!")

def get_anchor(text) -> str:
    result = ''
    d = []
    pattern = r'\b\s*(\d+)\s*/\s*(\d+)\s*/\s*(\d+)\s*\b'

    text = text.split('\n')

    for ind,val in enumerate(text):
        res = re.search(pattern, val) and formatted_date not in val
        if res:
            d.append(ind)
            # print(val,ind)

    for i in text[d[0]:]:
        result = result +  str(i) + '\n'
    
    # print(result)
    return result


def handle_prices(text) -> str:
    pattern = r'(\w+)\s*-\s*(\d+\.\d+)'

    matches = re.findall(pattern, text)

    
    
    for match in matches:
        new_price = str(int(match[1].replace('.',''))*8)
        new_price = new_price[:-3] + "." +  new_price[-3:]
        # print(f" Extracted number: {match[1]} new price {new_price}")

        #!handle prices
        text = text.replace(match[1],str(new_price))
    
    # print(text)
    return text


async def main(msg_id:int):
    messages = []
    f = open('test.json','a',encoding='utf-8')
    async with app:
        async for msg in  app.get_chat_history(-1001291236326):
            if msg.text!=None:
                if formatted_date in msg.text and msg.id==msg_id:
                    text = msg.text
                    answer = get_anchor(text)
                    answer = handle_prices(answer)
                    await app.send_message("me",answer)


async def get_keyboard():
    products_dict = {}
    async with app:
        async for msg in  app.get_chat_history(-1001291236326):
            if msg.text!=None:
                if 'Официальный аккаунт' in msg.text and '@BSASeller' in msg.text:
                    # print(msg.reply_markup.inline_keyboard)
                    for i in msg.reply_markup.inline_keyboard:
                        for j in i:
                            print(j.text,j.url)
                    



                

# app.run(get_keyboard())
app.run(main(12118))