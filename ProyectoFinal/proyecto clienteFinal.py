from Tkinter import *
import socket
import threading
from threading import *
'''En esta parte se inicializa lo que es la ventana principal del programa de manera grafica
junto al socket el cual se conecta al otro programa para enviar y recibir informacion'''
mi_socket=socket.socket()
raiz=Tk()
raiz.title("Cocina")
frame=Frame(raiz, width=500, height=400)
frame.pack()
#---se importa el socket para conectarlo con el servidor del mesero---#
while True:
	try:
		mi_socket.connect(("localhost",8000))
		break
	except:
		continue
#-------------------------------Funciones--------------------------------#		
#Funcion que recibe datos#
def listen():
	global mi_socket
	da=StringVar()
	#Este prceso es que manda la informacion a cada uno de las listas correspondientes#
	#Se tiene que mantener en un ciclo infinito pues estara reciviendo informacion constantemente
	while True:
		try:
			da=mi_socket.recv(1024)
			while True:
				#informacion para la mesa 1
				if da=="1":
					while True:
						try:
							da=mi_socket.recv(1024)
							if da=="1":
								continue
							elif da=="2" or da=="3" or da=="4" or da=="5":
								break
							else:
								impresion.insert(END,da)
						except:
							continue
				#informacion para la mesa 2									
				elif da=="2":
					while True:
						try:
							da=mi_socket.recv(1024)
							if da=="2":
								continue
							elif da=="1" or da=="3" or da=="4" or da=="5":
								break
							else:
								impresion2.insert(END,da)
						except:
							continue
				#informacion para la mesa 3			
				elif da=="3":
					while True:
						try:
							da=mi_socket.recv(1024)
							if da=="2":
								continue
							elif da=="2" or da=="1" or da=="4" or da=="5":
								break
							else:
								impresion3.insert(END,da)
						except:
							continue
				#informacion para la mesa 4
				elif da=="4":
					while True:
						try:
							da=mi_socket.recv(1024)
							if da=="4":
								continue
							elif da=="2" or da=="3" or da=="1" or da=="5":
								break
							else:
							
								impresion4.insert(END,da)
						except:
							continue
				#informacion para la mesa 5
				elif da=="5":
					while True:
						try:
							da=mi_socket.recv(1024)
							if da=="5":
								continue
							if da=="2" or da=="3" or da=="4" or da=="1":
								break
							else:
								impresion5.insert(END,da)
						except:
							continue
				else:
					continue													
		except:
			continue
			'''esta funcion recibe los datos del mesero para que los valla imprimiendo
			en las lista definidas'''
#------------------------#
def remove(list):
	list.delete(1,END)#esta funcion solo borra las lista para dejarlas en blanco
#Funcion que envia datos al mesero#

#-----Funcion para notificar-----#
def send(numero):
	global mi_socket

	while True:
		try:
			mi_socket.send("La orden de la mesa "+numero+" esta lista")
			break
		except:
			continue
	'''Esta funcion envia la notificacion al mesero de sobre que orden de mesa esta lista'''
#----------- --------------------grafica--------------------------------#
#En esta parte solamente son solo funciones para por las variables y las entradas de una manera grafica
#Ponerle tilulos, declarar botones, etc 
comanda=Label(frame,text="comandas")
comanda.grid(row=0,column=0)

impresion=Listbox(frame)
impresion.grid(row=1,column=1)
impresion.insert(0,"1")

boton=Button(frame, text="Notificar", command=lambda:send("1"))#este boton sirve para notificar al mesero de la orden
boton.config(cursor="hand2")
boton.pack()
boton.grid(row=2,column=1)
botonD=Button(frame, text="remove", command=lambda:remove(impresion))#este boton sirve para borrar la comanda
botonD.config(cursor="hand2")
botonD.pack()
botonD.grid(row=3,column=1)

impresion2=Listbox(frame)
impresion2.grid(row=1,column=2)
impresion2.insert(0,"2")
boton=Button(frame, text="Notificar", command=lambda:send("2"))#este boton sirve para notificar al mesero de la orden
boton.config(cursor="hand2")
boton.pack()
boton.grid(row=2,column=2)

botonD2=Button(frame, text="remove", command=lambda:remove(impresion2))#este boton sirve para borrar la comanda
botonD2.config(cursor="hand2")
botonD2.pack()
botonD2.grid(row=3,column=2)

impresion3=Listbox(frame)
impresion3.grid(row=1,column=3)
impresion3.insert(0,"3")
boton=Button(frame, text="Notificar", command=lambda:send("3"))#este boton sirve para notificar al mesero de la orden
boton.config(cursor="hand2")
boton.pack()
boton.grid(row=2,column=3)

botonD3=Button(frame, text="remove", command=lambda:remove(impresion3))#este boton sirve para borrar la comanda
botonD3.config(cursor="hand2")
botonD3.pack()
botonD3.grid(row=3,column=3)

impresion4=Listbox(frame)
impresion4.grid(row=4,column=1)
impresion4.insert(0,"4")
boton=Button(frame, text="Notificar", command=lambda:send("4"))#este boton sirve para notificar al mesero de la orden
boton.config(cursor="hand2")
boton.pack()
boton.grid(row=5,column=1)

botonD4=Button(frame, text="remove", command=lambda:remove(impresion4))#este boton sirve para borrar la comanda
botonD4.config(cursor="hand2")
botonD4.pack()
botonD4.grid(row=6,column=1)

impresion5=Listbox(frame)
impresion5.grid(row=4,column=2)
impresion5.insert(0,"5")
boton=Button(frame, text="Notificar", command=lambda:send("5"))#este boton sirve para notificar al mesero de la orden
boton.config(cursor="hand2")
boton.pack()
boton.grid(row=5,column=2)

botonD5=Button(frame, text="remove", command=lambda:remove(impresion5))#este boton sirve para borrar la comanda
botonD5.config(cursor="hand2")
botonD5.pack()
botonD5.grid(row=6,column=2)


if __name__ == "__main__" :
	Thread(target=listen).start()



raiz.mainloop()