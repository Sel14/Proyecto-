from Tkinter import *
import ttk
import socket
import threading
from threading import *


#---se crea el servidor---#
mi_socket=socket.socket()
mi_socket.bind(("localhost",8000))
mi_socket.listen(1)
#---titulos---#
raiz=Tk()
raiz.title("comandas")
frame=Frame(raiz, width=500, height=400)
frame.pack(fill="both",expand="True")
#---variables---#
tablet=StringVar()
producto1=StringVar()
producto2=StringVar()
producto3=StringVar()
producto4=StringVar()

come=StringVar()
n1=StringVar()
n2=StringVar()
n3=StringVar()
n4=StringVar()
temporal=StringVar()
temporal2=StringVar()

#---llenado temporal---#
#tac.set(" ")
#torta.set(" ")
#corte.set(" ")
#tablet.set(" ")
#come.set(" ")
n1.set(" ")
n2.set(" ")
n3.set(" ")
n4.set(" ")
temporal.set(" ")
temporal2.set(" ")
#-------------------------------todas las funciones-----------------------------#
#---socket---#
while True:
	try:
		conexion,addr=mi_socket.accept()
		break
	except:
		continue
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
	send(producto1,n1)
	send(producto2,n2)
	send(producto3,n3)
	send(producto4,n4)
	send(come,temporal2)
#---send---#
def send(data,n):
	global mi_socket
	global conexion,addr
	while True:
		if data.get()!=(" ") and n.get()!=(" "):
			try:
				conexion.send(data.get()+" cantidad "+n.get())
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
#---listen---#
def listen():
	global mi_socket
	global conexion,addr
	da=StringVar()
	

	while True:
		try:
			da=conexion.recv(1024)
			llamada.insert(END,da)
		except:
			continue
#--------------------------------------Menu------------------------------------#		
#----titulos---#
producto=Label(frame,text="producto")
producto.grid(row=1,column=1)
cantidad=Label(frame,text="cantidad")
cantidad.grid(row=1,column=2)
#---mesa---"#
mesa=Label(frame, text="No.Mesa:")
mesa.grid(row=0,column=0)
tablet=ttk.Combobox(frame,textvariable=tablet)
tablet["values"]=["1","2","3","4","5"]
tablet.grid(row=0,column=1)
#---tacos---#
Tacos=Label(frame, text="Tacos:")
Tacos.grid(row=2,column=0)
producto1=ttk.Combobox(frame,textvariable=producto1)
producto1["values"]=["Asado","Churrasco","Pollo","Chorizo argentino","Arrachera"]
producto1.grid(row=2,column=1)
cantidad1=Entry(frame,textvariable=n1)
cantidad1.grid(row=2,column=2)
#---tortas---#
Tortas=Label(frame, text="Tortas:")
Tortas.grid(row=3,column=0)
producto2=ttk.Combobox(frame,textvariable=producto2)
producto2["values"]=["Choripan","Torta de Churrasco","Media churrasco","chistorra","Asado","Hamburguesa"]
producto2.grid(row=3,column=1)
cantidad2=Entry(frame,textvariable=n2)
cantidad2.grid(row=3,column=2)
#---cortes---#
Cortes=Label(frame, text="Cortes:")
Cortes.grid(row=4,column=0)
producto3=ttk.Combobox(frame,textvariable=producto3)
producto3["values"]=["Churrasquito de lomo","Pollo al chimi","Churrasco Angus","Asado de tira","Arrachera angus","Picana","Bife de chorizo"]
producto3.grid(row=4,column=1)
cantidad3=Entry(frame,textvariable=n3)
cantidad3.grid(row=4,column=2)
#---parrilladas---#
parrilladas=Label(frame, text="Parrilladas:")
parrilladas.grid(row=5,column=0)
producto4=ttk.Combobox(frame,textvariable=producto4)
producto4["values"]=["Parrilada de 3 carnes","Parrillada argentina","Parrillada especial"]
producto4.grid(row=5,column=1)
cantidad4=Entry(frame,textvariable=n4)
cantidad4.grid(row=5,column=2)
#---comentarios---#
comentarios=Label(frame,text="Comentarios")
comentarios.grid(row=6,column=0,)
texto=Entry(frame,textvariable=come)
texto.grid(row=6,column=1)
#---boton y guardar datos---#
boton=Button(raiz, text="Agregar", command=guarda)
boton.config(cursor="hand2")
boton.pack()
boton2=Button(raiz, text="Enviar", command=Enviar)
boton2.config(cursor="hand2")
boton2.pack()	
#---impresion---#
'''impresion=Listbox(frame)
impresion.grid(row=7,column=1)'''
#---llamada---#
llamada=Listbox(frame)
llamada.grid(row=7,column=2)
#---scroll---#
'''scroll=Scrollbar(frame,command=impresion.yview)
scroll2=Scrollbar(frame,command=impresion.xview,orient="horizontal")
scroll.grid(row=7,column=2,sticky="nws")
scroll2.grid(row=8,column=1,sticky="ew")
impresion.config(yscrollcommand=scroll.set)
impresion.config(xscrollcommand=scroll2.set)'''
#---scroll de la llamada---#
scroll3=Scrollbar(frame,command=llamada.xview,orient="horizontal")
scroll3.grid(row=8,column=2,sticky="ew")
llamada.config(xscrollcommand=scroll3.set)
#---Thread---#
if __name__ == "__main__" :
	Thread(target=listen).start()


raiz.mainloop()