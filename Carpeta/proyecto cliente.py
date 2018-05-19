from Tkinter import *
import socket
import threading
from threading import *

mi_socket=socket.socket()
raiz=Tk()
raiz.title("Cocina")
frame=Frame(raiz, width=500, height=400)
frame.pack(fill="both",expand="True")
#---import socket---#
while True:
	try:
		mi_socket.connect(("localhost",8000))
		break
	except:
		continue
#-------------------------------Funciones--------------------------------#		
def listen():
	global mi_socket
	da=StringVar()
	while True:
		try:
			da=mi_socket.recv(1024)
			impresion.insert(END,da)
		except:
			continue			
def send():
	global mi_socket

	while True:
		try:
			mi_socket.send("La orden de la mesa "+impresion.get(0)+" esta lista")
			break
		except:
			continue
comanda=Label(frame,text="comanda")
comanda.grid(row=0,column=0)

impresion=Listbox(frame)
impresion.grid(row=1,column=1)

boton=Button(raiz, text="Notificar", command=send)
boton.config(cursor="hand2")
boton.pack()

if __name__ == "__main__" :
	Thread(target=listen).start()



raiz.mainloop()