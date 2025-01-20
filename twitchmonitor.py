import requests
import time

TWITCH_CLIENT_ID = ""
TWITCH_ACCESAS_TOKEN = ""
CHANNEL_NAME = "" #Streamer you want to monitor
CHECK_INTERVAL = 600

HEADERS = {
    "Client-ID": TWITCH_CLIENT_ID,
    "Authorization": f"Bearer {TWITCH_ACCESAS_TOKEN}",
}

def isChanelLive(channel_name):
    url = f"https://api.twitch.tv/helix/streams?user_login={channel_name}"
    response = requests.get(url, headers = HEADERS)

    if response.status_code == 200:
        data = response.json()
        return len(data.get("data", [])) > 0 #If theres data here, the chanel is live
    else:
        print(f"Fail to connect to the API: {response.status_code} - {response.text}")
        return False
    

def main():
    
    while True:
        try:
            live = isChanelLive(CHANNEL_NAME)
            if live:
                print(f"{CHANNEL_NAME} is streaming right now")
            else:
                print(f"{CHANNEL_NAME} is not streaming right now") 

        except Exception as e:
            print("Something went wrong: {e}")

        time.sleep(CHECK_INTERVAL)   
