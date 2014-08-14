#!/bin/python


#lez be able to grab some sweet sweet json and do stuffs with it
import json

# you would not believe the amount of hours I wasted getting this PoS to work. I HATE you, requests.
# If you keep getting dumb errors that the requests module isn't found, you'll have to install it.
# if it still fails, just place the requests folder in the same directory
import requests
import getpass
from pprint import pprint

# grab the creds of the user
print ("\n\n\n\n")
print ("THERE EH TIS, THE BRIDGE OF DEATH")
print ("ASK ME THE QUESTIONS, BRIDGEKEEPER. I AM NOT AFRAID.")
print ("\n\n\n\n")
user=input("VRUT, IS YOUR NAME?  ")

# TODO yeah, I freaking get it. possible kaplain text. yammer yammer yammer. It's a demo, yo.
passwd = getpass.getpass("VRUT, IS YOUR .... PASSWORD?  ")


# ALRIGHT ALRIGHT ALRIIIIIGHT.  /watch?v=zsmkfLhtX24
# Let's pass the login data to log this baby in.
# CREDIT: blog.tankorsmash.com/?p=295 for helping get a firm footing here

# pass creds and define api type
user_pass_dict = {'user': user, 'passwd': passwd, 'api_type':'json'}

# Reddit wants us to give a custom User Agent so that they know we're an App
headers = {'user-agent':'Reddindum App. github/sharteries/reddindum' }

# Session. Good type of beer and good type of user-action handling
# but this also assures that we're keeping our session open for each action
# which is especially important for it sending our user agent each call.
client = requests.session()
client.headers = headers

# Send it off ... into the mystic ... /watch?v=rq53NkUZAT0
# TODO error handling of login failures
r = client.post(r'http://www.reddit.com/api/login', data=user_pass_dict)

# parse the json response to a python dict for easier data handling.
# You'll see me use the 'decode' function again, and it's because it's being read as bytes
# and I want to parse this puppy as strings (at first)
j = json.loads(r.content.decode('utf-8'))

# grab the modhash
client.modhash = j['json']['data']['modhash']


# For testing, let's make sure it works, but in the future obviously don't print it.
# TODO remove this line.
print ('{user}\'s modhash is totes: {mh}'.format(user=user, mh=client.modhash))

# Notify the user of successful login!
print ('\n\nYou\'re all logged in!\n\n')
