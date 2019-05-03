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

## known issues & todos
Please refer to the [issues list](https://github.com/mkmozgawa/telegren/issues).
