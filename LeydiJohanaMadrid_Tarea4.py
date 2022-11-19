import tkinter #Librería para interfaz gráfica
from tkinter import messagebox

def guardarDatos(): 
    if entradaId.get() == "" or entradaNombre.get() == "" or entradaEdad.get() == "" or entradaPais.get() == "" or entradaTelefono.get() == "" or entradaFecha.get() == "":
        messagebox.showinfo(message="Diligenciar todos los campos 🤔", title="Error")
    else:
        messagebox.showinfo(message="Datos enviados 😁", title="Mensaje")

    

Ventana = tkinter.Tk()
Ventana.geometry('400x400') #Tamaño de la ventana
Ventana.title("Usuarios") #Cambiar nombre de la ventana
Ventana.configure(background='#F8F8F8') #Cambiar color de la ventana


labelTitulo = tkinter.Label(Ventana, text="Usuarios", font=('Poppins', 20, 'bold'), fg='#2274A5', pady=1, background='#F8F8F8')
labelTitulo.grid(row=1, column=1)

labelId = tkinter.Label(Ventana, text="Id: ", font=('Poppins', 11), fg='#404040', padx=70, background='#F8F8F8')
labelId.grid(pady=5, row=2, column=0)

entradaId = tkinter.Entry(Ventana, font=('Poppins', 10))
entradaId.grid(row=2, column=1)

labelNombre = tkinter.Label(Ventana, text="Nombre: ", font=('Poppins', 11), fg='#404040', background='#F8F8F8')
labelNombre.grid(pady=5, row=3, column=0)

entradaNombre = tkinter.Entry(Ventana, font=('Poppins', 10))
entradaNombre.grid(row=3, column=1)

labelEdad = tkinter.Label(Ventana, text="Edad: ", font=('Poppins', 11), fg='#404040', background='#F8F8F8')
labelEdad.grid(pady=5, row=4, column=0)

entradaEdad = tkinter.Entry(Ventana, font=('Poppins', 10))
entradaEdad.grid(row=4, column=1)

labelPais = tkinter.Label(Ventana, text="País: ", font=('Poppins', 11), fg='#404040', background='#F8F8F8')
labelPais.grid(pady=5, row=5, column=0)

entradaPais = tkinter.Entry(Ventana, font=('Poppins', 10))
entradaPais.grid(row=5, column=1)

labelTelefono = tkinter.Label(Ventana, text="Teléfono: ", font=('Poppins', 11), fg='#404040', background='#F8F8F8')
labelTelefono.grid(pady=5, row=6, column=0)

entradaTelefono = tkinter.Entry(Ventana, font=('Poppins', 10))
entradaTelefono.grid(row=6, column=1)

labelFecha = tkinter.Label(Ventana, text="Fecha: ", font=('Poppins', 11), fg='#404040', background='#F8F8F8')
labelFecha.grid(pady=5, row=7, column=0)

entradaFecha = tkinter.Entry(Ventana, font=('Poppins', 10))
entradaFecha.grid(row=7, column=1)

botonGuardarDatos = tkinter.Button(Ventana, text="Guardar datos", font=('Poppins', 11), bg='#2274A5', fg='#FFFFFF', width=17, command=guardarDatos, activebackground="#3681AC", activeforeground='#FFFFFF')
botonGuardarDatos.grid(pady=5, row=8, column=1)



Ventana.mainloop() #Esta línea debe de ir al final del código