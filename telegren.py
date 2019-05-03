import telegram
import json
import time
import sys

from setup import create_file, read_file, TOKEN_FILE, KEYWORD_FILE, REPLY_FILE, OFFSET_FILE

def create_bot(token):
    ''' Return a bot instance. '''
    try:
        return telegram.Bot(token=token)
    except telegram.error.InvalidToken:
        print("Invalid token. I know you've tried your best, though.")
        sys.exit(1)

def fetch_updates(bot, offset):
    ''' Return the newest updates (based off the offset value) if possible. If there are new updates return None. '''
    try:
        updates = bot.get_updates(offset=offset)
        if len(updates) > 0:
            return updates
        else:
            return None
    except telegram.error.TimedOut:
        return None

def run_bot():

    TOKEN = read_file(TOKEN_FILE)
    KEYWORD = read_file(KEYWORD_FILE)
    REPLY = read_file(REPLY_FILE)
    OFFSET = read_file(OFFSET_FILE)

    bot = create_bot(TOKEN)

    while True:
        updates = fetch_updates(bot, OFFSET)
        if updates is not None:
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
    
