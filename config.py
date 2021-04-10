import os
import json
from dotenv import load_dotenv
load_dotenv()

channel_input = os.getenv('CHATINPUT')
channel_input = [int(i) for i in channel_input.split(' ')] 
channel_output = os.getenv('CHATOUTPUT')
REDISTOGO_URL = os.getenv('REDISTOGO_URL')

session = os.getenv("SESSION")
api_hash = os.getenv("API_HASH")
api_id = os.getenv("API_ID")
