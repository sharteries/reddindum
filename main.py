#!/bin/python

# let's be able to push our authentication along with keeping access to our session
import auth

# interface our db
import dbinter

# TODO decide if these still need to be called since we're importing other files that already use them.
# They were put here originally for testing without the auth and dbinter files.
import json
import requests
from pprint import pprint

# Ask what they want to do. Just simple stuff for now.
print ('\nYes, me Lord?\n')
print ('1. Follow a new thread (live threads included)')
print ('2. Get followed threads')

choice = input("\nEnter a number: ")

if (choice == '1'):
	# So, here we can just ask the user to give us the base32 ID and we're good to go!
	thread = input("\nEnter thread ID: ")
	url = "http://www.reddit.com/comments/"+thread+"/.json"
	# Grab the json file with our creds/session
	r = auth.client.get(url)

	# put it into an easy to edit format
	j = json.loads(r.content.decode('utf-8'))

	# navigate down to the value that we need
	comcount = j[0]['data']['children'][0]['data']['num_comments']

	# Here, we let the user give a unique name to the thread if they want to call it later
	custom = input("\nIf you want a custom name for the thread, enter it here: ")

	# if they decide on nothing, make it "null" so that sqlite doesn't freak out
	if (custom == ""):
		custom = "null"
	dbinter.insert_thread(custom, thread, comcount, comcount)
	dbinter.print_thread()

	# TODO remove this later, but this is just to test to make sure our session is still
	# on, and that we're not pulling data without a useragent and such, thus getting flagged
	# as possible spam
	print (j[0]['data']['modhash'])
elif (choice == '2'):
	#TODO database stuffs
	print ('\nokay')
else:
	#TODO again, I get it. Input validation and whatnot. Just a demo :)
	print ('\nJust the integer bro. Only a 1, or a 2. Or go bless yourself')
	print ('I mean, yeah, I could easily strip the period or accept loose inputs, but eh')
