from estudiantes import estudiantes

def MenuPrincipal():
    while True:
        print("----------MENU PRINCIPAL----------")
        print("1. estudiantes")
        print("2. salir")
        
        opcion_x = int(input("escoja una opcion: "))
        
        if opcion_x==1:
            x=estudiantes
            print(x.editor())
        elif opcion_x==2:
            print("adios")
            break
        else:
            print("escoja una opcion de la lista")
            continue

MenuPrincipal()