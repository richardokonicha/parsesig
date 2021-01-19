import os
from dotenv import load_dotenv
load_dotenv()

channel_input = os.getenv('CHATINPUT')
channel_input = [int(i) for i in channel_input.split(' ')]  # dont
channel_output = int(os.getenv('CHATOUTPUT')) # dont

session = os.getenv("SESSION")
api_hash = os.getenv("API_HASH")
api_id = os.getenv("API_ID")

def save_session(client, session):
    if session:
        pass
    else:
        session_string = client.session.save()
        env_string = f"SESSION = {session_string}"
        with open(".env", "a") as env_file:
            env_file.write(env_string)
