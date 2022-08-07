from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


app = Flask(__name__)
# LINE BOT info
# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('Hjqhh20tlTgXZmmPkGExqEEoSzN6KjUHVyzQO28lOGoIhiLTCFLcj0vtK9+o3O+Eukh7FZe2oz/FlPHJwHkcWGrj5L5rksyjtNWK6PFO4Jd2VJnWPyXwHlrnw3X6RYVJm0p1F5lHMdYvtRhtZtonCgdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('aca3f81b11da59002969d3fcbe0e5564')

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    print(body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# # Message event
# @handler.add(MessageEvent)
# def handle_message(event):
#     message_type = event.message.type
#     user_id = event.source.user_id
#     reply_token = event.reply_token
#     message = event.message.text
#     line_bot_api.reply_message(reply_token, TextSendMessage(text = message))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port)
