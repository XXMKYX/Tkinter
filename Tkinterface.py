#Importa libreria con todo el contenido
from tkinter import*
from tkcalendar import DateEntry
import pandas as pd

#Asignacion interface
root = Tk()
#Personalizacion ventana
root.title("SCI") #titulo
root.geometry("700x800") #Dimensiones
#root.iconbitmap("SCI.ico") #Icono
root.resizable(0,0) #Desactivamos opcion para modificar ventana
root.config(bg="#900C3F",cursor="arrow") #color y tipo de cursor

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
#name.set("Name")
saludo = StringVar()

texto1 = Label(root,text="Ingresa tu nombre", bd=4,font="arial 12") #texto
texto1.place(x=20,y=150)
input1 = Entry(root,textvariable=name,bd=4,font="arial 12")
input1.place(x=180,y=150)

def saludos():
    print("Greatings to " + name.get())
    saludo.set("Greatings to " + name.get())

    

buttonName = Button(root,text="Saludame!",bd=5,command = saludos,bg="red")
buttonName.place(x=20,y=200)
out1 = Entry(root,text="Greatings to " + name.get(),state="disable",textvariable=saludo,bd=4,font="arial 12") #State inmodificable
out1.place(x=180, y=200)

#DATAFRAME
Nombre = StringVar()
nombre = StringVar()
Nombre2 = StringVar()
Apellido = StringVar()
Apellido2 = StringVar()
Sede = StringVar()
Folio = StringVar()
Registro = StringVar()
Vigencia = StringVar()
Empleado = StringVar()
#TITLE
textTitle = Label(root,text="Sistema de credenciales para la UTEyCV", bd=4,font="arial 16",bg="#900C3F",fg="#fff")
textTitle.place(x=20,y=200)
#FORM
textNombre = Label(root,text="Nombre:", bd=4,font="arial 12",bg="#900C3F",fg="#fff")
textNombre.place(x=20,y=250)
inNombre = Entry(root,textvariable=Nombre,bd=4,font="arial 12",bg="#CFCFCF",fg="#000")
inNombre.place(x=150,y=250)
textNombre2 = Label(root,text="Nombre 2:", bd=4,font="arial 12",bg="#900C3F",fg="#fff")
textNombre2.place(x=20,y=300)
inNombre2 = Entry(root,textvariable=Nombre2,bd=4,font="arial 12",bg="#CFCFCF",fg="#000")
inNombre2.place(x=150,y=300)
textApellido = Label(root,text="Apellido:", bd=4,font="arial 12",bg="#900C3F",fg="#fff")
textApellido.place(x=20,y=350)
inApellido = Entry(root,textvariable=Apellido,bd=4,font="arial 12",bg="#CFCFCF",fg="#000")
inApellido.place(x=150,y=350)
textApellido2 = Label(root,text="Apellido 2:", bd=4,font="arial 12",bg="#900C3F",fg="#fff")
textApellido2.place(x=20,y=400)
inApellido2 = Entry(root,textvariable=Apellido2,bd=4,font="arial 12",bg="#CFCFCF",fg="#000")
inApellido2.place(x=150,y=400)
textSede = Label(root,text="Sede:", bd=4,font="arial 12",bg="#900C3F",fg="#fff")
textSede.place(x=20,y=450)
inSede = Entry(root,textvariable=Sede,bd=4,font="arial 12",bg="#CFCFCF",fg="#000")
inSede.place(x=150,y=450)
textFolio = Label(root,text="Folio:", bd=4,font="arial 12",bg="#900C3F",fg="#fff")
textFolio.place(x=20,y=500)
inFolio = Entry(root,textvariable=Folio,bd=4,font="arial 12",bg="#CFCFCF",fg="#000")
inFolio.place(x=150,y=500)
textRegistro = Label(root,text="Registro:", bd=4,font="arial 12",bg="#900C3F",fg="#fff")
textRegistro.place(x=20,y=550)
inRegistro = Entry(root,textvariable=Registro,bd=4,font="arial 12",bg="#CFCFCF",fg="#000")
inRegistro.place(x=150,y=550)
textVigencia = Label(root,text="Vigencia:", bd=4,font="arial 12",bg="#900C3F",fg="#fff")
textVigencia.place(x=20,y=600)
inVigencia = Entry(root,textvariable=Vigencia,bd=4,font="arial 12",bg="#CFCFCF",fg="#000")
inVigencia.place(x=150,y=600)
textEmpleado = Label(root,text="Empleado:", bd=4,font="arial 12",bg="#900C3F",fg="#fff")
textEmpleado.place(x=20,y=650)
inEmpleado = Entry(root,textvariable=Empleado,bd=4,font="arial 12",bg="#CFCFCF",fg="#000")
inEmpleado.place(x=150,y=650)

def save():
    datos = [
        Nombre.get(),
        Nombre2.get(),
        Apellido.get(),
        Apellido2.get(),
        Sede.get(),
        Folio.get(),
        Registro.get(),
        Vigencia.get(),
        Empleado.get()
    ]
    print(datos)
    DFDatosRaw = pd.DataFrame(datos)
    print(DFDatosRaw)
    DFDatosRaw2 = DFDatosRaw.transpose()
    print(DFDatosRaw2)

    saved = Label(root,text="Registro guardado!",bg="yellow")
    saved.pack()

    clear()

def clear():
    inNombre.delete("0","end")
    inNombre2.delete("0","end")
    inApellido.delete("0","end")
    inApellido2.delete("0","end")
    inSede.delete("0","end")  
    inFolio.delete("0","end")
    inRegistro.delete("0","end")
    inVigencia.delete("0","end")
    inEmpleado.delete("0","end")

buttonName = Button(root,text="Guardar Datos",bd=3,command = save,bg="#94FF40",font="arial 12",cursor="plus")
buttonName.place(x=20,y=700)


#Cierre de la ventana hasta que lo indiquemos
root.mainloop()

