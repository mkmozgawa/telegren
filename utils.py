import telegram
import sys

''' Util functions used by other files. '''

def create_file(filename, value):
    with open(filename, 'w') as f:
        try:
            f.write(value)
        except TypeError:
            f.write(str(value))

def read_file(filename):
    with open(filename, 'r') as f:
        content = f.read().strip()
    return content

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

def process_updates(updates, bot, KEYWORD, REPLY, OFFSET):
    ''' Process the updates. '''
    for update in updates:
        try:
            message = update.message.text
            if message is not None and KEYWORD in message.lower():
                chat_id = update.message.chat_id
                bot.send_message(chat_id=chat_id, text=REPLY)
        except AttributeError: # raised when it can't process a message (sticker, image, etc)
            continue

def get_offset(updates):
    ''' Return the offset after processing the most recent messages. +1 so the next query only asks for the messages that haven't been processed yet. '''
    return updates[-1].update_id + 1