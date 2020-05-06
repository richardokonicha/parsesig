import telethon
import os
from flask import Flask, request
import telebot
from telebot import types
from parser import pasig
server = Flask(__name__)
TOKEN = os.getenv("TOKEN")
URL = os.getenv("URL")
TOKEN="852053528:AAHL_ryUUJ1JOhenzmI0WDiayAnxxqGFmyU"
URL="https://test1335.herokuapp.com/"
# URL="https://d4ed5f94.ngrok.io/"




bot = telebot.TeleBot(TOKEN, threaded=True)

@bot.message_handler(commands=["begin"])
def begin(message):
    chat_id = message.chat.id
    text = "this is the start"
    bot.send_message(
        chat_id,
        text=text
    )

@bot.channel_post_handler(commands=None, regexp=None, func=lambda message: message.content_type == "text",content_types=None)
def begin_chan(message):
    chat_id = message.chat.id
    rawsignal = message.text
    signal = pasig(rawsignal)
    raw_id = -1001313782946
    if signal:
        bot.send_message(
            chat_id,
            text=signal,
            parse_mode="html"
        )
    else:
        pass

@server.route("/"+TOKEN, methods=['POST'])
def getMessage():
    request_object = request.stream.read().decode("utf-8")
    update_to_json = [telebot.types.Update.de_json(request_object)]
    bot.process_new_updates(update_to_json)
    return "got Message bro"

@server.route("/hook")
def webhook():
    url=URL
    bot.remove_webhook()
    bot.set_webhook(url + TOKEN)
    return f"Webhook set to {url}"
# bot.get_chat_members_count

# bot.remove_webhook()
# bot.polling()
if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))