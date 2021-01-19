import os
import telebot
from dotenv import load_dotenv
load_dotenv()

test_output = int(os.getenv("TESTOUTPUT"))
bot_session = os.getenv("bot_session")
bot = telebot.TeleBot(bot_session)


def bot_forward(text):
    bot.send_message(test_output, text)
    pass
