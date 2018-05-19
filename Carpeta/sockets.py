import socket
import time
import threading
from threading import *
mi_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

mi_socket.bind(("",8000))
mi_socket.listen(5)

while True:
	conexion,addr =mi_socket.accept()
	print"conexion establecida"+ str(addr)
	break
	
	
def listen():
	global mi_socket
	global conexion,addr
	while True:
		data= conexion.recv(1024) 
		print ("hola")

def send():
	global mi_socket
	global conexion,addr

	while True:
		msg=raw_input()
		conexion.send(msg)


if __name__=="__main__":
	Thread(target=listen).start()
	Thread(target=send).start()
