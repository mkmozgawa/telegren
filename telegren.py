import telegram
import json
import time

from setup import create_file, read_file, TOKEN_FILE, KEYWORD_FILE, REPLY_FILE, OFFSET_FILE

def run_bot():

    TOKEN = read_file(TOKEN_FILE)
    KEYWORD = read_file(KEYWORD_FILE)
    REPLY = read_file(REPLY_FILE)
    OFFSET = read_file(OFFSET_FILE)

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

            create_file(OFFSET_FILE, OFFSET)
        
        time.sleep(1)

if __name__ == "__main__":
    run_bot()
    
