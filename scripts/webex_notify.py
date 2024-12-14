import requests

WEBEX_TEAMS_TOKEN = "NjhkNDViZGYtMjJjZi00OWUzLTgxMDYtODM0MGVlMzQ2YjE0NmE0ZDI2OWEtNjdm_P0A1_652b5f1d-9846-4334-8b83-52d9cf3b9b81"
ROOM_ID = "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vYzMyMzJjNzAtYmEzNS0xMWVmLTliNTktNjM1ZTdlOTNmMTEw"

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
