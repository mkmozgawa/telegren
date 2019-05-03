import telegram
import time

from setup import TOKEN_FILE, KEYWORD_FILE, REPLY_FILE, OFFSET_FILE
from utils import create_file, read_file, create_bot, fetch_updates, process_updates, get_offset

def run_bot():

    TOKEN = read_file(TOKEN_FILE)
    KEYWORD = read_file(KEYWORD_FILE)
    REPLY = read_file(REPLY_FILE)
    OFFSET = read_file(OFFSET_FILE)

    bot = create_bot(TOKEN)

    while True:
        updates = fetch_updates(bot, OFFSET)
        if updates is not None:
            process_updates(updates, bot, KEYWORD, REPLY, OFFSET)
            OFFSET = get_offset(updates)
            create_file(OFFSET_FILE, OFFSET)
        
        time.sleep(1)

if __name__ == "__main__":
    run_bot()
    
