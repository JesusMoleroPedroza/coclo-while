import tkinter as tk
#funciones
def mostrar():
    frame=tk.Frame(ventana,width=200,height=200)
    frame.config(borderwidth=3,relief="solid")
    frame.grid(row=6,column=0)
    fnom=tk.Label(frame,text="nombre:")
    fape=tk.Label(frame,text="apellido:")
    feda=tk.Label(frame,text="edad:")
    fsex=tk.Label(frame,text="sexo:")
    fciu=tk.Label(frame,text="ciudad:")
    
    fnom.place(x=0,y=0)
    fape.place(x=0,y=20)
    feda.place(x=0,y=40)
    fsex.place(x=0,y=60)
    fciu.place(x=0,y=80)
    
    rnom=tk.Label(frame,text=textnombre.get())
    rape=tk.Label(frame,text=textapellido.get())
    reda=tk.Label(frame,text=textedad.get())
    rsex=tk.Label(frame,text=opcion.get())
    rciu=tk.Label(frame,text=rciudad.get(rciudad.curselection()))
    
    rnom.place(x=50,y=0)
    rape.place(x=50,y=20)
    reda.place(x=50,y=40)
    rsex.place(x=50,y=60)
    rciu.place(x=50,y=80)
    
    
    

#ventana
ventana=tk.Tk()
ventana.title("mi primera ventana")
ventana.geometry("500x800")

#label´s y text´s
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
opcion=tk.StringVar()
rsexoM=tk.Radiobutton(ventana,text="Male",state="normal",variable=opcion,value="masculino")
rsexoM.grid(row=3,column=1)
rsexoF=tk.Radiobutton(ventana,text="Female",state="normal",variable=opcion,value="femenino")
rsexoF.grid(row=3,column=2)

ciudad=tk.Label(ventana,text="ciudad:")
ciudad.grid(row=4,column=0)
rciudad=tk.Listbox(ventana,width=20)
elementos=["cartagena","bogota","barranquilla"]
for elemento in elementos:
    rciudad.insert(tk.END, elemento)
rciudad.grid(row=4,column=1)

#boton
boton=tk.Button(ventana,text="registrar",command=mostrar)
boton.grid(row=5,column=1)

ventana.mainloop()