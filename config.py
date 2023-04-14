import os
import json
from dotenv import load_dotenv
load_dotenv()

chinput2 = os.getenv('CHATINPUT2')

chinput = os.getenv('CHATINPUT')
# chinput = '-1001221682168 -1001942212599'
channel_input = [int(i) for i in chinput.split(' ')]
channel_input.append(int(chinput2))

choutput = os.getenv('CHATOUTPUT')
# choutput = '-1001907605122'
channel_output = [int(i) for i in choutput.split(' ')]

REDIS_URL = os.getenv('REDIS_URL')

session = os.getenv("SESSION")
api_hash = os.getenv("API_HASH")
api_id = os.getenv("API_ID")
sentry_env = os.getenv("SENTRY_ENV")
