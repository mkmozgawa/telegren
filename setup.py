from utils import create_file

TOKEN_FILE = "token.txt"
KEYWORD_FILE = "keyword.txt"
REPLY_FILE = "reply.txt"
OFFSET_FILE = "offset.txt"
EXCLUSION_FILE = 'excluded.txt'
OFFSET_VALUE_INITIAL = "0"

''' This file contains the setup script'''

def setup_bot():
    print("Setup time! Please don't lie to me, I'd know.")
    token = input("My bot token: ")
    keyword = input("The keyword I should react to: ")
    reply = input("My witty response whenever the keyword appears in the conversation: ")

    excluded = []
    exclusion = "word"
    while exclusion != '':
        exclusion = input("Is there any word you'd like to me to ignore?")
        print("Sure! I'm going to pretend I haven't heard anyone saying '{}'!".format(exclusion))
        if exclusion != '':
            excluded.append(exclusion + '\n')

    create_file(TOKEN_FILE, token)
    create_file(KEYWORD_FILE, keyword)
    create_file(REPLY_FILE, reply)
    create_file(OFFSET_FILE, OFFSET_VALUE_INITIAL)
    create_file(EXCLUSION_FILE, excluded)

    print("Setup complete! You may now run telegren.py.")

if __name__ == "__main__":
    setup_bot()

