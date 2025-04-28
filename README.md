<h2> Twitch live monitor </h2>
  This is a python script to monitor if a twitch streamer is live. 

<h2 >📝 Requirements </h2>
  <a href="https://www.python.org/downloads/">• Python</a><br/>
  <a href="https://pypi.org/project/pip/">• Pip</a><br/>
  <a href="https://dev.twitch.tv/">• Twitch API access</a>  

## 🛠️ Setting up 
  After obtaining your `client_id` and `client_secret`, update the variables in the `gettoken.py` file and run the script using the following command:
  
    $ python3 gettoken.py
    
  If everything was set up correctly, you will receive your `TWITCH_ACCESS_TOKEN`. Make sure to save it.

## 🚀 Running
  In the `twitchmonitor.py` file, update the following variables:
     
   `TWITCH_CLIENT_ID` = "your client id"  
   `TWITCH_ACCESS_TOKEN` = "your access token"  
   `CHANNEL_NAME` = "the channel you want to monitor"

  Once all variables are updated, run the following command to start the script:

  ```
  $ python3 twitchmonitor.py
```
  Enjoy the script!
