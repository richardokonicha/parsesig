import os
import json
from dotenv import load_dotenv
load_dotenv()


chinput = os.getenv('CHATINPUT')
chinput = '-1001799753250 -1001574745581 -1001322515232 -1001725353361'
channel_input = [int(i) for i in chinput.split(' ')]
choutput = os.getenv('CHATOUTPUT')
choutput = '-1001802541407'
channel_output = [int(i) for i in choutput.split(' ')]


REDIS_URL = os.getenv('REDIS_URL')

session = os.getenv("SESSION")
api_hash = os.getenv("API_HASH")
api_id = os.getenv("API_ID")
sentry_env = os.getenv("SENTRY_ENV")
