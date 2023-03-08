#Importa libreria con todo el contenido
from tkinter import*
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

texto0 = Label(root,text="Sistema de credenciales para la UTEyCV", bd=4,font="arial 16",bg="#900C3F",fg="#fff")
texto0.place(x=20,y=200)

texto1 = Label(root,text="Nombre:", bd=4,font="arial 12",bg="#900C3F",fg="#fff")
texto1.place(x=20,y=250)
input1 = Entry(root,textvariable=Nombre,bd=4,font="arial 12",bg="#CFCFCF",fg="#000")
input1.place(x=150,y=250)
texto2 = Label(root,text="Nombre 2:", bd=4,font="arial 12",bg="#900C3F",fg="#fff")
texto2.place(x=20,y=300)
input2 = Entry(root,textvariable=Nombre2,bd=4,font="arial 12",bg="#CFCFCF",fg="#000")
input2.place(x=150,y=300)
texto3 = Label(root,text="Apellido:", bd=4,font="arial 12",bg="#900C3F",fg="#fff")
texto3.place(x=20,y=350)
input3 = Entry(root,textvariable=Apellido,bd=4,font="arial 12",bg="#CFCFCF",fg="#000")
input3.place(x=150,y=350)
texto4 = Label(root,text="Apellido 2:", bd=4,font="arial 12",bg="#900C3F",fg="#fff")
texto4.place(x=20,y=400)
input4 = Entry(root,textvariable=Apellido2,bd=4,font="arial 12",bg="#CFCFCF",fg="#000")
input4.place(x=150,y=400)
texto5 = Label(root,text="Sede:", bd=4,font="arial 12",bg="#900C3F",fg="#fff")
texto5.place(x=20,y=450)
input5 = Entry(root,textvariable=Sede,bd=4,font="arial 12",bg="#CFCFCF",fg="#000")
input5.place(x=150,y=450)
texto6 = Label(root,text="Folio:", bd=4,font="arial 12",bg="#900C3F",fg="#fff")
texto6.place(x=20,y=500)
input6 = Entry(root,textvariable=Folio,bd=4,font="arial 12",bg="#CFCFCF",fg="#000")
input6.place(x=150,y=500)
texto7 = Label(root,text="Registro:", bd=4,font="arial 12",bg="#900C3F",fg="#fff")
texto7.place(x=20,y=550)
input7 = Entry(root,textvariable=Registro,bd=4,font="arial 12",bg="#CFCFCF",fg="#000")
input7.place(x=150,y=550)
texto8 = Label(root,text="Vigencia:", bd=4,font="arial 12",bg="#900C3F",fg="#fff")
texto8.place(x=20,y=600)
input8 = Entry(root,textvariable=Vigencia,bd=4,font="arial 12",bg="#CFCFCF",fg="#000")
input8.place(x=150,y=600)
texto9 = Label(root,text="Empleado:", bd=4,font="arial 12",bg="#900C3F",fg="#fff")
texto9.place(x=20,y=650)
input9 = Entry(root,textvariable=Empleado,bd=4,font="arial 12",bg="#CFCFCF",fg="#000")
input9.place(x=150,y=650)

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

def clear():
    input1.delete("1.0","end")

    

buttonName = Button(root,text="Guardar Datos",bd=3,command = save,bg="#94FF40",font="arial 12",cursor="plus")
buttonName.place(x=20,y=700)


#Cierre de la ventana hasta que lo indiquemos
root.mainloop()

