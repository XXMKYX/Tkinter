#Importa libreria con todo el contenido
from tkinter import*
#Asignacion interface
root = Tk()
#Personalizacion ventana
root.title("SCI") #titulo
root.geometry("500x300") #Dimensiones
#root.iconbitmap("SCI.ico") #Icono
root.resizable(0,0) #Desactivamos opcion para modificar ventana
root.config(bg="grey",cursor="circle") #color y tipo de cursor

#BOTONES
button1 = Button(root,text="Minimizar",command = root.iconify,bg="green") #Minimiza el borton
button1.pack(side=RIGHT) #Posiciona el boton en la ventana
#Funcion para imprimir
def imprimir():
    print("Printing...")
    label1 = Label(root,text="Printing...")
    label1.pack()

button2 = Button(root,text="Print",command = imprimir,bg="pink")
button2.pack(side=LEFT)


texto = Label(root,text="PROOF") #texto
texto.pack() #Asignacion del texto a la ventana

#Cierre de la ventana hasta que lo indiquemos
root.mainloop()