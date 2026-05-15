import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()


account_sid =  os.environ.get("TWILIO_ACCOUNT_SID")
auth_token =os.environ.get("TWILIO_AUTH_TOKEN")
MY_PHONE = os.environ.get("MY_PHONE")

client = Client(account_sid, auth_token)

app_id = os.environ.get("APP_KEY")

parameters =\
    {"appid": app_id,
     "lat" : 52.5200,
     "lon" : 13.4050,

     # "lat":35.6895,
     # "lon": 139.6917,

     # "lat":33.4484	,
     # "lon":-112.0740,

     "units" : "metric",
     "cnt": 6,
     }

get_data = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
get_data.raise_for_status()
one_code = get_data.json()["list"]
codes_for_day = [item["weather"][0]["id"] for item in one_code]
# print(codes_for_day)
need_umbrella = False
for i in codes_for_day:
    if i < 600:
        need_umbrella = True
    else:
       pass

if need_umbrella:
    print("Bring umbrella")
    message = client.messages.create(
        body='It is going to be rainy',
        from_='+12523903135',
        to=MY_PHONE,)

    print(message.sid)
