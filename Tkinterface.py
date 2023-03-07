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

texto = Label(root,text="SCI") #texto
texto.pack() #Asignacion del texto a la ventana

#Cierre de la ventana hasta que lo indiquemos
root.mainloop()