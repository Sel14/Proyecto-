from Tkinter import *
import socket
import sys
import time
import threading
from threading import *

mi_socket=socket.socket()
mi_socket.bind (("localhost",8000))
mi_socket.listen(1)
#---titulos---#
raiz=Tk()
raiz.title("comandas")
frame=Frame(raiz, width=500, height=400)
frame.pack(fill="both",expand="True")
#---socket---#
while True:
	try:
		conexion,addr=mi_socket.accept()
		break
	except:
		continue
#---variables---#
tac = StringVar()
torta=StringVar()
corte=StringVar()
parrillada=StringVar()
tablet= StringVar()
come=StringVar()
n1=StringVar()
n2=StringVar()
n3=StringVar()
n4=StringVar()
temporal=StringVar()
temporal2=StringVar()
#---llenado temporal---#
tac.set(" ")
torta.set(" ")
corte.set(" ")
tablet.set(" ")
come.set(" ")
n1.set(" ")
n2.set(" ")
n3.set(" ")
n4.set(" ")
temporal.set(" ")
temporal2.set(" ")
#-------------------------------todas las funciones-----------------------------#
#---funciones---#
def guarda ():
	comand(tablet)
	comand(tac)
	comand(torta)
	comand(corte)
	comand(parrillada)
	comand(come)

	'''reset(tablet)
	reset(tac)
	reset(torta)
	reset(corte)
	reset(parrillada)
	reset(come)'''
def comand(data):
	impresion.insert(END, data.get())
def reset(da):
	da.set(" ") 
def Enviar():
	send(tablet,temporal)
	send(tac,n1)
	send(torta,n2)
	send(corte,n3)
	send(parrillada,n4)
	send(come,temporal2)
#---socket---#
def send(data,n):
	global mi_socket
	global conexion,addr
	while True:
		if data.get()!=(" ") and n.get()!=(" "):
			try:
				conexion.send(data.get()+" "+"cantidad"+" "+n.get())
				data.set(" ")
				n.set(" ")
				break
			except:
				continue
		elif data.get()!=(" "):
				try:
					conexion.send(data.get())
					data.set(" ")
					n.set(" ")
					break
				except:
					continue
		else:
			break
#----titulos---#
producto=Label(frame,text="producto")
producto.grid(row=1,column=1)
cantidad=Label(frame,text="cantidad")
cantidad.grid(row=1,column=2)
#---mesa---"#
mesa=Label(frame, text="No.Mesa:")
mesa.grid(row=0,column=0)
cantidadMe=Entry(frame,textvariable=tablet)
cantidadMe.grid(row=0,column=1)
#---tacos---#
Tacos=Label(frame, text="Tacos:")
Tacos.grid(row=2,column=0)
producto1=Entry(frame,textvariable=tac)
producto1.grid(row=2,column=1)
cantidad1=Entry(frame,textvariable=n1)
cantidad1.grid(row=2,column=2)
#---tortas---#
Tortas=Label(frame, text="Tortas:")
Tortas.grid(row=3,column=0)
producto2=Entry(frame,textvariable=torta)
producto2.grid(row=3,column=1)
cantidad2=Entry(frame,textvariable=n2)
cantidad2.grid(row=3,column=2)
#---cortes---#
Cortes=Label(frame, text="Cortes:")
Cortes.grid(row=4,column=0)
producto3=Entry(frame,textvariable=corte)
producto3.grid(row=4,column=1)
cantidad3=Entry(frame,textvariable=n3)
cantidad3.grid(row=4,column=2)
#---parrilladas---#
parrilladas=Label(frame, text="Parrilladas:")
parrilladas.grid(row=5,column=0)
producto4=Entry(frame,textvariable=parrillada)
producto4.grid(row=5,column=1)
cantidad4=Entry(frame,textvariable=n4)
cantidad4.grid(row=5,column=2)
#---comentarios---#
comentarios=Label(frame,text="Comentarios")
comentarios.grid(row=6,column=0,)
texto=Entry(frame,textvariable=come)
texto.grid(row=6,column=1)
#texto.geometry(width=60, height=30)
#texto.pack()
#---boton y guardar datos---#
boton=Button(raiz, text="Agregar", command=guarda)
boton.config(cursor="hand2")
boton.pack()
boton2=Button(raiz, text="Enviar", command=Enviar)
boton2.config(cursor="hand2")
boton2.pack()	
#---impresion---#
impresion=Listbox(frame)
impresion.grid(row=7,column=1)
#---scroll---#
scroll=Scrollbar(frame,command=impresion.yview)
scroll2=Scrollbar(frame,command=impresion.xview,orient="horizontal")
scroll.grid(row=7,column=2,sticky="nws")
scroll2.grid(row=8,column=1,sticky="ew")
impresion.config(yscrollcommand=scroll.set)
impresion.config(xscrollcommand=scroll2.set)


raiz.mainloop()