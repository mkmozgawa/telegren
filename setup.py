TOKEN_FILE = "token.txt"
KEYWORD_FILE = "keyword.txt"
REPLY_FILE = "reply.txt"
OFFSET_FILE = "offset.txt"
OFFSET_VALUE_INITIAL = "0"

''' This file contains the setup script along with some helper functions. '''

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

def setup_bot():
    print("Setup time! Please don't lie to me, I'd know.")
    token = input("My bot token: ")
    keyword = input("The keyword I should react to: ")
    reply = input("My witty response whenever the keyword appears in the conversation: ")

    create_file(TOKEN_FILE, token)
    create_file(KEYWORD_FILE, keyword)
    create_file(REPLY_FILE, reply)
    create_file(OFFSET_FILE, OFFSET_VALUE_INITIAL)

    print("Setup complete! You may now run telegren.py.")

if __name__ == "__main__":
    setup_bot()
