import pyrogram
from pyrogram import Client,filters
from pyrogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,InlineKeyboardButton)
import toml
from datetime import datetime
import json
import traceback
import re

PRODUCTS = []
today = datetime.today()
formatted_date_msg = today.strftime("%d/%m/%Y")
formatted_date = today.strftime("%Y-%m-%d")

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


    # text = text.split('\n')

    # for ind,val in enumerate(text):
    #     res = re.search(pattern, val)
    #     if res:
    #         d.append(ind)
    #         print(val,ind)

    # for i in text[d[1]:]:
    #     result = result +  str(i) + '\n'
    
    # print(result)
    return text.split(' +12 месяцев - 10.000₽')[-1]


def handle_prices(text) -> str:
    pattern = r'(\w+)\s*-\s*(\d+\.\d+)'

    matches = re.findall(pattern, text)

    
    
    for match in matches:
        new_price = str(int(match[1].replace('.',''))*10)
        new_price = new_price[:-3] + "." +  new_price[-3:]
        # print(f" Extracted number: {match[1]} new price {new_price}")

        #!handle prices
        text = text.replace(match[1],str(new_price))
    
    # print(text)
    return text

def create_product_dict():
    global PRODUCTS
    f = open('product_list.txt',encoding='utf-8').readlines()
    for i in f:
        PRODUCTS.append(i.replace(' ','_').replace('\n',''))



async def main(msg_id,app):
        async for msg in  app.get_chat_history(CONFIG['target_chat_id']):
            if msg.id == msg_id:
                print('msg_edit_date:',msg.edit_date,'today',formatted_date,'date equal:',(formatted_date in str(msg.edit_date)) or (formatted_date_msg in msg.text))
            if msg.text!=None:
                if ((formatted_date in str(msg.edit_date)) or (formatted_date_msg in msg.text)) and msg.id==msg_id:
                    text = msg.text
                    answer = get_anchor(text)
                    answer = handle_prices(answer)
                    # print('answer',answer)
                    await app.send_message(CONFIG['userbot_chat_id'],answer)


async def get_keyboard(word,app) -> int:
    print(word)
    async for msg in  app.get_chat_history(CONFIG['target_chat_id']):
        if msg.text!=None:
            if 'Официальный аккаунт' in msg.text and '@BSASeller' in msg.text:
                # print(msg.reply_markup.inline_keyboard)
                for i in msg.reply_markup.inline_keyboard:
                    for j in i:
                        # print(j.text,j.url)
                        if word.lower() in j.text.lower():
                            # print('msg_id:',str(j.url).split('/')[-1])
                            return int(str(j.url).split('/')[-1])
                    


@app.on_message()
async def message_handler(client,message):
    global PRODUCTS
    try:
        # print(message.sender_chat.id)
        if message.sender_chat.id == CONFIG['userbot_chat_id']:
            print(message.text.replace('/','',1) in PRODUCTS)
            if message.text == "/help":
                help_text = 'HELP MESSAGE\n'
                for i in PRODUCTS:
                    help_text+=f'/{i}\n'
                print(help_text)
                await app.send_message(message.sender_chat.id,help_text)

            
            if message.text.replace('/','',1) in PRODUCTS:
                print('work',message.text.replace('/','',1).replace('_',' '))
                msg_ig = await get_keyboard(message.text.replace('/','',1).replace('_',' '),app)
                print('msg_id',msg_ig)
                await main(msg_ig,app)
    except:
        # traceback.print_exc()
        pass

if __name__ == '__main__':
    create_product_dict()
    app.run()