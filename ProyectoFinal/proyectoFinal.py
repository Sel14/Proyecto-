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
'''frame=Frame(raiz, width=500, height=400)
frame.pack(fill="both",expand="True")'''


def on_configure(event):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    canvas.configure(scrollregion=canvas.bbox('all'))



# --- create canvas with scrollbar ---

canvas = Canvas(raiz)
canvas.pack(side=LEFT)

scrollbar = Scrollbar(raiz, command=canvas.yview)
scrollbar.pack(side=LEFT, fill='y')

canvas.configure(yscrollcommand = scrollbar.set)

# update scrollregion after starting 'mainloop'
# when all widgets are in canvas
canvas.bind('<Configure>', on_configure)

# --- put frame in canvas ---

frame = Frame(canvas,width=500, height=400)
canvas.create_window((0,0), window=frame, anchor='nw')

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
def reset(da):
	da.set(" ") 
def Enviar():
	if tablet.get()=="1":
		agregar(producto1,n1,impresion)
		agregar(producto2,n2,impresion)
		agregar(producto3,n3,impresion)
		agregar(producto4,n4,impresion)
		agregar(come,temporal2,impresion)
	elif tablet.get()=="2":
		agregar(producto1,n1,impresion2)
		agregar(producto2,n2,impresion2)
		agregar(producto3,n3,impresion2)
		agregar(producto4,n4,impresion2)
		agregar(come,temporal2,impresion2)
	elif tablet.get()=="3":
		agregar(producto1,n1,impresion3)
		agregar(producto2,n2,impresion3)
		agregar(producto3,n3,impresion3)
		agregar(producto4,n4,impresion3)
		agregar(come,temporal2,impresion3)
	elif tablet.get()=="4":
		agregar(producto1,n1,impresion4)
		agregar(producto2,n2,impresion4)
		agregar(producto3,n3,impresion4)
		agregar(producto4,n4,impresion4)
		agregar(come,temporal2,impresion4)
	elif tablet.get()=="5":
		agregar(producto1,n1,impresion5)
		agregar(producto2,n2,impresion5)
		agregar(producto3,n3,impresion5)
		agregar(producto4,n4,impresion5)
		agregar(come,temporal2,impresion5)
	else:
		pass

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
def remove(lista,numero):
	lista.delete(numero,END)
def agregar(data,n,lista):
	if data.get()!=(" ") and n.get()!=(" "):
		lista.insert(END,data.get()+" cantidad "+n.get())
	elif data.get()!=(" "):
		lista.insert(END,data.get())
	else:
		pass
				

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
boton2=Button(frame, text="Enviar", command=Enviar)
boton2.config(cursor="hand2")
boton2.pack()
boton2.grid(row=7,column=1)	
#---llamada---#
llamada=Listbox(frame)
llamada.grid(row=7,column=2)

boton3=Button(frame, text="Borrar", command=lambda:remove(llamada,0))
boton3.config(cursor="hand2")
boton3.pack()
boton3.grid(row=9,column=2)	
#---scroll de la llamada---#
scroll3=Scrollbar(frame,command=llamada.xview,orient="horizontal")
scroll3.grid(row=8,column=2,sticky="ew")
llamada.config(xscrollcommand=scroll3.set)
#---mesas---#
impresion=Listbox(frame)
impresion.grid(row=10,column=1)
impresion.insert(0,"1")

botonD=Button(frame, text="remove", command=lambda:remove(impresion,1))
botonD.config(cursor="hand2")
botonD.pack()
botonD.grid(row=11,column=1)

impresion2=Listbox(frame)
impresion2.grid(row=10,column=2)
impresion2.insert(0,"2")

botonD2=Button(frame, text="remove", command=lambda:remove(impresion2,1))
botonD2.config(cursor="hand2")
botonD2.pack()
botonD2.grid(row=11,column=2)

impresion3=Listbox(frame)
impresion3.grid(row=12,column=1)
impresion3.insert(0,"3")

botonD3=Button(frame, text="remove", command=lambda:remove(impresion3,1))
botonD3.config(cursor="hand2")
botonD3.pack()
botonD3.grid(row=13,column=1)

impresion4=Listbox(frame)
impresion4.grid(row=12,column=2)
impresion4.insert(0,"4")

botonD4=Button(frame, text="remove", command=lambda:remove(impresion4,1))
botonD4.config(cursor="hand2")
botonD4.pack()
botonD4.grid(row=13,column=2)

impresion5=Listbox(frame)
impresion5.grid(row=14,column=1)
impresion5.insert(0,"5")

botonD5=Button(frame, text="remove", command=lambda:remove(impresion5,1))
botonD5.config(cursor="hand2")
botonD5.pack()
botonD5.grid(row=15,column=1)

#---Thread---#
if __name__ == "__main__" :
	Thread(target=listen).start()


raiz.mainloop()