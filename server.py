#!/usr/bin/env python

'''
	Simple socket server using threads
''' 
import socket
import sys
from thread import *

def getDir():
	import os
	result = []
	for filename in os.listdir("."):
		result.append(filename)
	
	files = ""
	for f in result:
		files += '%s\n' % (f)
	
	return files
	
	
HOST = ''	# Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
#Bind socket to local host and port
try:
	s.bind((HOST, PORT))
except socket.error as msg:
	print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()
	 
print 'Socket bind complete'
 
#Start listening on socket
s.listen(10)
print 'Socket now listening'
 
#Function for handling connections. This will be used to create threads
def clientthread(conn,addr):
	#Sending message to connected client
	conn.send('Bienvenido al servidor de MARduino\n') #send only takes string
	 
	#infinite loop so that function do not terminate and thread do not end.
	try:
		while True: 
			#Receiving from client
			data = conn.recv(1024)
			if not data: 
				break
				
			print 'FROM %s:%s %s' %(addr[0], str(addr[1]), data)  
			
			responseData = data

			if data=="EOF<<":
				responseData = "Fin de conexion"
				
			elif data=="ll":
				responseData = "jjjjjjjj"
				
			elif data=="dir":
				responseData = getDir()
				
			reply = 'OK [%s]' % (responseData)
			conn.sendall(reply)	   

			if data=="EOF<<":
				 break
				 
				 
	except:
		#came out of loop
		print 'Excepcion from' + addr[0] + ':' + str(addr[1])	
		
	
	#came out of loop
	print 'EXIT from ' + addr[0] + ':' + str(addr[1])		
	conn.close()
	
 
#now keep talking with the client
while True:
	#wait to accept a connection - blocking call
	conn, addr = s.accept()
	print 'Connected with ' + addr[0] + ':' + str(addr[1])
		 
	#start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
	start_new_thread(clientthread ,(conn,addr))
		
s.close()
