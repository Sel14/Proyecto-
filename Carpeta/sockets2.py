import socket
import time
import threading
from threading import Thread
mi_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


while True:
	mi_socket.connect(("localhost",8000))
	print"conexion establecida"
	
	break
	

def listen():

	global mi_socket
	
	while True:
		data=mi_socket.recv(1024) 
		print data


def send():
	print ("hola")
	global mi_socket

	while True:
		msg=raw_input()
		mi_socket.send(msg)


if __name__ == "__main__" :
	Thread(target=send).start()
	Thread(target=listen).start()
	

