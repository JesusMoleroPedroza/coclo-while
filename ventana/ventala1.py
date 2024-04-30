import tkinter as tk

ventana=tk.Tk()

ventana.title("mi primera ventana")

ventana.geometry("500x800")

nombre=tk.Label(ventana,text="nombre:")
nombre.grid(row=0,column=0)
textnombre=tk.Entry(ventana,width=20)
textnombre.grid(row=0,column=1)

apellido=tk.Label(ventana,text="apellido:")
apellido.grid(row=1,column=0)
textapellido=tk.Entry(ventana,width=20)
textapellido.grid(row=1,column=1)

edad=tk.Label(ventana,text="edad:")
edad.grid(row=2,column=0)
textedad=tk.Entry(ventana,width=20)
textedad.grid(row=2,column=1)

sexo=tk.Label(ventana,text="sexo:")
sexo.grid(row=3,column=0)
rsexoM=tk.Radiobutton(ventana,text="Male",state="normal",variable="opcion",value=1)
rsexoM.grid(row=3,column=1)
rsexoF=tk.Radiobutton(ventana,text="Female",state="normal",variable="opcion",value=2)
rsexoF.grid(row=3,column=2)

ciudad=tk.Label(ventana,text="ciudad:")
ciudad.grid(row=4,column=0)
rciudad=tk.Listbox(ventana,width=20)
elementos=["cartagena","bogota","barranquilla"]
for elemento in elementos:
    rciudad.insert(tk.END, elemento)
rciudad.grid(row=4,column=1)

boton=tk.Button(ventana,text="registrar")
boton.grid(row=5,column=1)

ventana.mainloop()