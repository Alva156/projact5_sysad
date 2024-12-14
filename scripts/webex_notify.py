import requests

WEBEX_TEAMS_TOKEN = "your_webex_bot_token"
ROOM_ID = "your_room_id"

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
