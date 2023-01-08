import os
import json
from dotenv import load_dotenv
load_dotenv()

chinput = os.getenv('CHATINPUT')
channel_input = [int(i) for i in chinput.split(' ')] 
choutput = os.getenv('CHATOUTPUT')
channel_output = [int(i) for i in choutput.split(' ')] 


REDIS_URL = os.getenv('REDIS_URL')

session = os.getenv("SESSION")
api_hash = os.getenv("API_HASH")
api_id = os.getenv("API_ID")
