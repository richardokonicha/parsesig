import os
import json
from dotenv import load_dotenv
load_dotenv()

chinput = os.getenv('CHATINPUT')
chinput2 = os.getenv('CHATINPUT2')
channel_input = [int(i) for i in chinput.split(' ')]
if chinput2:
    channel_input.append(int(chinput2))

choutput = os.getenv('CHATOUTPUT')
choutput2 = os.getenv('CHATOUTPUT2')
channel_output = [int(i) for i in choutput.split(' ')]
if choutput2:
    channel_output.append(int(choutput2))

REDIS_URL = os.getenv('REDIS_URL')
session = os.getenv("SESSION")
api_hash = os.getenv("API_HASH")
api_id = os.getenv("API_ID")
sentry_env = os.getenv("SENTRY_ENV")

FILTER = os.getenv('FILTER')
