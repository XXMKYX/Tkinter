#Importa libreria con todo el contenido
from tkinter import*
#Asignacion interface
root = Tk()
#Personalizacion ventana
root.title("SCI") #titulo
root.geometry("700x500") #Dimensiones
#root.iconbitmap("SCI.ico") #Icono
root.resizable(0,0) #Desactivamos opcion para modificar ventana
root.config(bg="grey",cursor="circle") #color y tipo de cursor

#BOTONES
button1 = Button(root,text="-",command = root.iconify,bg="green") #Minimiza el borton
button1.place(x=180,y=50) #Posiciona el boton en la ventana
etiqueta1 = Label(root,text="Preciona para minimizar: ")
etiqueta1.place(x=20,y=50)
#Funcion para imprimir
def imprimir():
    print("Printing...")
    label1 = Label(root,text="Printing...")
    label1.pack()

button2 = Button(root,text="Print",command = imprimir,bg="pink")
button2.place(x=180,y=100)
etiqueta2 = Label(root,text="Preciona para imprimir: ")
etiqueta2.place(x=20,y=100)

#Organizacion por row y column
# .grid(row=0,column=1)

#Organizacion por coordenadas Place
# .place(x=90,y=50)

#Input

name = StringVar()
name.set("Name")
saludo = StringVar()

texto1 = Label(root,text="Ingresa tu nombre", bd=4,font="arial 12") #texto
texto1.place(x=20,y=180)
input1 = Entry(root,textvariable=name,bd=4,font="arial 12")
input1.place(x=180,y=180)

def saludos():
    print("Greatings to " + name.get())
    saludo.set("Greatings to " + name.get())

    

buttonName = Button(root,text="Saludame!",bd=5,command = saludos,bg="red")
buttonName.place(x=20,y=220)
out1 = Entry(root,text="Greatings to " + name.get(),state="disable",textvariable=saludo,bd=4,font="arial 12") #State inmodificable
out1.place(x=180, y=220)

#Cierre de la ventana hasta que lo indiquemos
root.mainloop()