import requests
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Fetch the variables from the .env file
WEBEX_TEAMS_TOKEN = os.getenv("WEBEX_TEAMS_TOKEN")
ROOM_ID = os.getenv("ROOM_ID")

def send_webex_message(message):
    url = "https://webexapis.com/v1/messages"
    headers = {
        "Authorization": f"Bearer {WEBEX_TEAMS_TOKEN}",
        "Content-Type": "application/json",
    }
    payload = {"roomId": ROOM_ID, "text": message}
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        print("Message sent to WebEx Teams.")
    else:
        print(f"Failed to send message: {response.status_code}")

if __name__ == "__main__":
    send_webex_message("Interface description updated successfully by NETCONF automation.")
