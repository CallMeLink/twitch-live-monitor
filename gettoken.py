import requests

url = "https://id.twitch.tv/oauth2/token"

data = {
    "client_id": "",
    "client_secret": "",
    "grant_type": "client_credentials",
}

response = requests.post(url, data = data)

if response.status_code == 200:
    token_info = response.json()
    print("Acess Token: ", token_info["access_token"])
else:
    print("Error ", response.status_code, response.text)