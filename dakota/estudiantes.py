class estudiantes:
    def editor():
        BD={}
        while True:
            print("\n---------Estudiantes----------")
            print("1. ver lista")
            print("2. crear")
            print("3. actualizar")
            print("4. eliminar")
            print("5. volver al menu principal")
            
            opcion = int(input("escoja una opcion: "))
            
            if opcion==1:
                print("\n-----------lista------------")
                for id, datos in BD.items():
                    print("ID:",id)
                    print("nombre:",datos[0],datos[1])
                    print("edad:",datos[2])
                    print("N. identificacion:",datos[3],"\n")
            
            elif opcion==2:
                print("\n----------crear----------")
                ID=int(input("escriba el id: "))
                nombre=input("escriba el nombre: ")
                apellido=input("escriba el apellido: ")
                edad=int(input("escriba la edad: "))
                cc=str(input("escriba el numero de identidad: "))
                
                if ID in BD:
                    print("ese ID ya esta en uso")
                    continue
                else:
                    
                    guardar=str(input("desea guardar los datos(si/no): "))
                    guardar.lower()
                    if guardar=='si':
                        BD[ID]=[nombre,apellido,edad,cc]
                        print("!datos guardados¡")
                    elif guardar=='no':
                        print("no se guardaron los datos")
                        continue
            
            elif opcion==3:
                print("\n----------actualizar----------")
                id_buscar=int(input("escriba el id del grupo de datos a modificar: "))
                print("datos:")
                print("1. nombre")
                print("2. apellido")
                print("3. edad")
                print("4. N. documento")
                selection=int(input("que dato va a modificar: "))
                
                if selection==1:
                    print("modificar nombre")
                    nombre_mod=str(input("escriba el nombre:"))
                    
                    guardar=str(input("desea guardar los datos(si/no): "))
                    guardar.lower()
                    if guardar=='si':
                        BD[id_buscar][0]=nombre_mod
                        print("!datos guardados¡")
                    elif guardar=='no':
                        print("no se guardaron los datos")
                        continue
                    
                elif selection==2:
                    print("modificar apellido")
                    apellido_mod=str(input("escriba el apellido:"))
                    
                    guardar=str(input("desea guardar los datos(si/no): "))
                    guardar.lower()
                    if guardar=='si':
                        BD[id_buscar][1]=apellido_mod
                        print("!datos guardados¡")
                    elif guardar=='no':
                        print("no se guardaron los datos")
                        continue
                    
                elif selection==3:
                    print("modificar edad")
                    edad_mod=int(input("escriba la edad:"))
                    
                    guardar=str(input("desea guardar los datos(si/no): "))
                    guardar.lower()
                    if guardar=='si':
                        BD[id_buscar][2]=edad_mod
                        print("!datos guardados¡")
                    elif guardar=='no':
                        print("no se guardaron los datos")
                        continue
                
                elif selection==4:
                    print("modificar N. documento")
                    cc_mod=str(input("escriba el N. documento:"))
                    
                    guardar=str(input("desea guardar los datos(si/no): "))
                    guardar.lower()
                    if guardar=='si':
                        BD[id_buscar][3]=cc_mod
                        print("!datos guardados¡")
                    elif guardar=='no':
                        print("no se guardaron los datos")
                        continue
            
            elif opcion==4:
                print("\n----------eliminar----------")
                id_del=int(input("escriba la id a eliminar: "))
                
                eliminar=str(input("esta seguro de eliminar estos datos(si/no): "))
                eliminar.lower()
                if eliminar=='si':
                    BD.pop(id_del)
                    print("!datos eliminados¡")
                elif eliminar=='no':
                    print("no se eliminaron los datos")
                    continue
                
            elif opcion==5:
                break