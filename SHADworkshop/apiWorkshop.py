import urllib
import json

from twilio.rest import TwilioRestClient
account_sid = "AC0bc4d9e88aae168a64c9e9b06c00f02f"
auth_token = "a4033dd912cfd78f6637d80c8e756e29"
client = TwilioRestClient(account_sid, auth_token)

key = "42933f02198e67ad49a35a54c1d4869b"
city = "Toronto"
url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + key

response = urllib.urlopen(url)

parsedData = json.loads(response.read())
desc = parsedData['weather'][0]['description']
temp = parsedData['main']['temp']

customMsg = '" Hey my cute little apples" - Ryan, 2k19 the weather in ' + str(city) + ' is ' + str(int(temp)-273) + 'C and ' + str(desc)
message = client.messages.create(to="6478659104", from_="6476965048", body=customMsg)
