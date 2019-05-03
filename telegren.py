import telegram
import json
import time

with open('token.txt', 'r') as t:
    TOKEN = t.read().strip()

with open('reply.txt', 'r') as r:
    REPLY = r.read().strip()

with open('keyword.txt', 'r') as k:
    KEYWORD = k.read().strip()

with open('offset.txt', 'r') as o:
    OFFSET = int(o.read().strip())

bot = telegram.Bot(token=TOKEN)

while True:
    try:
        updates = bot.get_updates(offset=OFFSET)
    except telegram.error.TimedOut:
        continue

    if len(updates) > 0:
        chat_id = updates[-1].message.chat_id
        OFFSET = updates[-1].update_id + 1

        for update in updates:
            try:
                message = update.message.text
                if message is not None and KEYWORD in message.lower():
                    bot.send_message(chat_id=chat_id, text=REPLY)
                    break
            except AttributeError:
                continue

        with open('offset.txt', 'w') as o:
            o.write(str(OFFSET))
        
    time.sleep(1)
    
