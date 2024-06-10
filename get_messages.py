import pyrogram
from pyrogram import Client,filters
from pyrogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,InlineKeyboardButton)
import toml
from datetime import datetime
import json
import traceback
import re

today = datetime.today()
formatted_date_msg = today.strftime("%d/%m/%Y")
formatted_date = today.strftime("%Y-%m-%d")

CONFIG = toml.load('CONFIG.toml')

api_id=CONFIG['api_id']
api_hash =CONFIG['api_hash']

app = Client("userbot",api_id=api_id,api_hash=api_hash)

async def get_messages():
    res = ''
    async with app:
        async for msg in  app.get_chat_history(CONFIG['target_chat_id']):
            if msg.text!=None:
                res = res + msg.text+'\n\n----------------- ID '+str(msg.id)+'\n\n'
    
    with open('test.txt','w',encoding='utf-8') as f:
        f.write(res)
                            

app.run(get_messages())