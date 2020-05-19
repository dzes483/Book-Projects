#!/usr/bin/python3
# umbrella_reminder.py - Checks the weather for the day and texts the user a
# message to pack their umbrella, if there is rain in the forecast.

import json
import requests
from twilio.rest import Client

# Preset values:
account_SID = 'SID'
auth_token = 'auth_token'
my_num = 'my_number'
twi_num = 'Twilio_number'
location = 'location'

def textmyself(message):
    client = Client(account_SID, auth_token)
    client.messages.create(body=message, from_=twi_num, to=my_num)

# Download the JSON data from openweathermap.org's API.
url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}....'
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
weather_data = json.loads(response.text)

# If there will be rain today, send a text message to pack an umbrella.
w = weather_data['list']
if (w[0]['weather'][0]['main']).upper() == 'RAIN':
    textmyself('Pack an umbrella!')
