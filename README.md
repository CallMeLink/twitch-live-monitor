<h2> Twitch live monitor </h2>
  This is a python script to monitor if a twitch streamer is live. 

<h2 >📝 Requirements </h2>
  <a href="https://www.python.org/downloads/">Python</a> •
  <a href="https://www.python.org/downloads/">Pip</a> •
  <a href="https://dev.twitch.tv/">Twitch API access</a>

## 🛠️ Setting up 
  After getting your `client_id` and `client_secret` you need to update you variables in the `gettoken.py` file and run the file using the following command below:
  
    $ python3 gettoken.py
    
  If everything was done correctly you will recieve your `TWITCH_ACCESAS_TOKEN` make sure to save this.

## 🚀 Running
  In the `twitchmonitor.py` update the following variable:
     
   `TWITCH_CLIENT_ID` = "your client id"  
   `TWITCH_ACCESS_TOKEN` = "your access token"  
   `CHANNEL_NAME` = "the channel you want to monitor"

     
