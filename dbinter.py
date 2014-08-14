#!/bin/python


# Balls to you, rethinkdb! HAHAHA, Aaaahahaha, *sniff* aaahhwwhhaaaa :'(
import sqlite3

# connect to your db file. If it doesn't exist, it'll be created.
connection = sqlite3.connect('follow.db')

# let's point to the actionable commands for brevity
c = connection.cursor()

#check if the threads and comments table has been created, and if not, create them

# 'custom text'  : instead of having to call a the unique thread ID, you can just name it something
# 'thread text'  : thread ID. "text" due to it being alphanumeric. Not as efficient, but works
# 'unread integer'  : unread (by you, the user) comments
# 'comcount integer'  : total amount of comments in the thread

c.execute('''CREATE TABLE if not exists threads
		(custom text, thread text, unread integer, comcount integer)''')

# Creating a "comments" table to deal with actions specific to comments, like grabbing most used words
# I feel like separating the actual thread IDs and their status from all the comments is more efficient

# 'thread text'  : thread ID. Used to correlate the actual thread to its comments within
# 'comment text'  : the actual comment itself

c.execute('''create table if not exists comments
		(thread text, comment text)''')


##### SO, something to note, here, is that I'm not closing the connection to the db.
##### This is probably a bad idea, but I feel like we could be making a frequent amount of calls
##### and I don't want to close the connection if it's just going to be re-opened.

# insert a new thread to follow and commit the changes to the db
def insert_thread(custom, thread, unread, comcount):
	c.execute("insert into threads values (?,?,?,?);",(custom, thread, unread, comcount))
	connection.commit()

# same for comments
def insert_comment(thread, comment):
	c.execute("insert into comments values (?,?);",(thread, comment))
	connection.commit()

# show all the threads you have
def print_thread():
	for row in c.execute('select * from threads'):
		print(row)

#### I haven't written a print for comments yet, due to the sheer size that it could be.
#### That, and there may not be a direct need to ever do this, as such data, for now, should
#### never be called en masse anyway; only accessed for analytics.
