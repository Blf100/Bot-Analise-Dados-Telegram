from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()


class TelegramBot:
    def  __init__(self):
        TOKEN = os.getenv("API_KEY")
        self.url = f"https://api.telegram.org/bot{TOKEN}/"

    
    def start(self):
        while True:
            update = self.get_message()
            messages = update['result']
            if messages:
                for message in messages:
                    try:
                        update_id = update['message_id']
                        chat_id = message['message']['from']['id']

                    except:
                        pass

    
    def get_message(self):
        link_request = f"{self.url}getUpdates?timeout=1000"
        result = requests.get(link_request)
        return json.loads(result.content)
