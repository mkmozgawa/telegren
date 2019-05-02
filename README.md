# telegren

A Telegram chatbot that detects a keyword in a conversation and responds with a witty comeback.

## requirements
- A Telegram bot TOKEN. Get yours from [The BotFather](https://telegram.me/botfather).
- Add your token to `token.txt`, keyword to watch out for to `keyword.txt`, reply phrase to `reply.txt` and set `offset.txt` to 0 (it will get updated after the first run).

## local development
`virtualenv venv`

`pip install -r requirements.txt`

## local run
`python telegren.py`

## known issues
- Using stickers in the conversation causes a parse error. This is mitigated by checking if `update.message.text` is not `None` but this should be handled more clearly.
- It only responds in the conversation with the most recent keyword use.

## todos
- Add a response counter to see how many times it hit you with its blunt bot force.
- Reply directly to the message that triggered the response.
- In the reply message point out to the word that tiggered the response.
- Add responding in any conversation as long as it's needed there. The truth cannot be silenced! XD
