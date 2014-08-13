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
print "\n\n\n\n"
print "THERE EH TIS, THE BRIDGE OF DEATH"
print "ASK ME THE QUESTIONS, BRIDGEKEEPER. I AM NOT AFRAID."
print "\n\n\n\n"
user=raw_input("VRUT, IS YOUR NAME?  ")

# TODO yeah, I feaking get it. plain text. yammer yammer yammer. It's a demo, yo.
passwd = getpass.getpass("VRUT, IS YOUR .... PASSWORD?  ")


# ALRIGHT ALRIGHT ALRIIIIIGHT.
# Let's pass the login data to log this baby in.
# CREDIT: blog.tankorsmash.com/?p=295 for helping get a firm footing here

# pass creds and define api type
user_pass_dict = {'user': user, 'passwd': passwd, 'api_type':'json'}

# Reddit wants us to give a custom User Agent so that they know we're an App
headers = {'user-agent':'Reddindum App. github/sharteries/reddindum' }

# Session. Good type of beer and good type of user-action handling
client = requests.session()
client.headers = headers

# Send it off ... into the mystic ... ?v=rq53NkUZAT0
# TODO error handling of login failures
r = client.post(r'http://www.reddit.com/api/login', data=user_pass_dict)

# parse the json response to a python dict for easier data handling
j = json.loads(r.content)

# grab the modhash
client.modhash = j['json']['data']['modhash']


# for testing, let's make sure it works
print '{user}\'s modhash is totes: {mh}'.format(user=user, mh=client.modhash)
print '\n\nYou\'re all logged in!\n\n'
