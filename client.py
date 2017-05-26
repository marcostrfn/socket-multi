#client example
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8888))

print "\nQ/q para Salir\n"
response = True

while 1:
	if response:
		data = client_socket.recv(1024)
	response = False	
	if ( data == 'q' or data == 'Q' or data == 'OK [Fin de conexion]' ):
		client_socket.close()
		break;
	else:
		print "$ " , data
		data = raw_input ( "\n> " )
		if (data <> 'Q' and data <> 'q'):
			# print "enviando (%s) " % (len(data))
			if len(data)>0:
				# print "enviando (%s) " % (len(data))
				client_socket.send(data)
				response = True
		else:
			client_socket.send(data)
			client_socket.close()
			break;