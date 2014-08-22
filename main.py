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
	def set_comment(id):
		comment = id['data']['body']
		com_id = id['data']['id']
		if id['data']['parent_id']:
			par_id = id['data']['parent_id']
		else:
			par_id = "annie"
		dbinter.insert_comment(thread, par_id, com_id, comment)
		#if id['data']['replies']:
		#	sub += 1
		#	get_comment(sub)
	def get_comment(sub):
		num = "a" + str(sub)
		r = i['data']['replies']['data']['children']
		while sub != "null": 
			for num in r:
				if "more" in num['kind']:
					pass
				else:
					set_comment(num)
				if num['data']['replies']:
					sub += 1
					num = "a" + str(sub)
					r = r.append(['data']['children'])
					#get_comment(sub)
				else:
					sub = "null"
					#pass
	# So, here we can just ask the user to give us the base32 ID and we're good to go!
	thread = input("\nEnter thread ID: ")
	url = "http://www.reddit.com/comments/"+thread+"/.json"#?sort=new"
	# Grab the json file with our creds/session
	r = auth.client.get(url)

	# put it into an easy to edit format
	j = json.loads(r.content.decode('utf-8'))

	# navigate down to the value that we need
	comcount = j[0]['data']['children'][0]['data']['num_comments']
	#for i in range (0,comcount - 1):
	#	comment = j[1]['data']['children'][i]['data']['body']
	count = 0
	for i in j[1]['data']['children']:
		if "more" in i['kind']:
			print ("Done.")
		else:
			# This was to just make sure it was pulling all the parent comments correctly
			#count += 1
			#comment = i['data']['body']
			#print ("======================")
			#print (comment)
			sub = 0
			set_comment(i)
			if i['data']['replies']:
				get_comment(sub)
				#if 
				#dir = ['data']['replies']['data']['children']
				#for x in i['data']['replies']['data']['children']:
				#	if "more" in x['kind']:
				#		pass
				#	else:
				#		set_comment()
						#comment = x['data']['body']
						#com_id = x['data']['id']
						#par_id = x['data']['parent_id']
						#dbinter.insert_comment(thread, par_id, com_id, comment)
						#print ("------")
						#print ("Reply:")
						#print (comment)
				
			#comment = i['data']['body']
			#if not thread in i['data']['parent_id']:
			#	print ("------")
			#	print ("Reply:")
			#else:
			#print ("======================")
			#print (comment)
			#print (count)
	# Here, we let the user give a unique name to the thread if they want to call it later
	custom = input("\nIf you want a custom name for the thread, enter it here: ")

	# if they decide on nothing, make it "null" so that sqlite doesn't freak out
	if (custom == ""):
		custom = "null"
	#dbinter.insert_thread(custom, thread, comcount, comcount)
	#dbinter.insert_comment(thread, com_id, comment)
	#dbinter.print_thread()
	dbinter.print_comments()
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

"""def set_comment():
	comment = i['data']['body']
	com_id = i['data']['id']
	if x['data']['parent_id']:
		par_id = x['data']['parent_id']
	else:
		par_id = "null"
	dbinter.insert_comment(thread, par_id, com_id, comment)"""
