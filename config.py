
import os
import json
from dotenv import load_dotenv
load_dotenv()

# chinput = '-1001236662259 -1001193424112'

chinput = os.getenv('CHATINPUT')
chinput2 = os.getenv('CHATINPUT2')
chinput3 = os.getenv('CHATINPUT3')
channel_input = [int(i) for i in chinput.split(' ')]
if chinput2: channel_input.append(int(chinput2))
if chinput3: channel_input.append(int(chinput3))

choutput = os.getenv('CHATOUTPUT')
# choutput = '-1001221680759'
channel_output = int(choutput)

REDIS_URL = os.getenv('REDIS_URL')

session = os.getenv("SESSION")
api_hash = os.getenv("API_HASH")
api_id = os.getenv("API_ID")
sentry_env = os.getenv("SENTRY_ENV")


# def save_session(client, session):
#     if session:
#         pass
#     else:
#         session_string = client.session.save()
#         env_string = f"\nSESSION = {session_string}"
#         with open(".env", "a") as env_file:
#             env_file.write(env_string)
