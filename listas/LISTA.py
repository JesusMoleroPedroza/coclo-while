#Jesus Molero.

#1. lista vacia.
lista = []

#2. lista con cinco elementos.
lista2 = [1,2,3,4,5]

#3. longitud de la lista.
print("la longitus de la lista es:", len(lista2))

#4. primer elemento, el elemento central y el último elemento de la lista.
print("primer elemento: ",lista2[0]," elemento central: ",lista2[2], "ultimo elemento: ",lista2[4])

#5. lista llamada tipos datos mezclados.
lista3 = ["jesus",20,1.76,"soltero","Bayunca"]

#6. variable de lista llamada it_companies y asígnele los valores iniciales.
it_companies = []
it_companies.insert(0, "Facebook")
it_companies.insert(1, "Google")
it_companies.insert(2, "Microsoft")
it_companies.insert(3, "Apple")
it_companies.insert(4, "IBM")
it_companies.insert(5, "Oracle")
it_companies.insert(6, "Amazon")
print(it_companies)

#7.  Añadir una empresa de TI a it_companies utilizando los metodos de insercion.
it_companies.append("Magnifix")
print(it_companies)

#8. Comprobar si una determinada empresa existe en la lista it_companies.
existe = 'Apple' in it_companies
print(existe)

#9. Ordena la lista con el método sort()
it_companies.sort()
print(it_companies)

#10. Invierte la lista en orden descendente utilizando el método reverse()
it_companies.reverse()
print(it_companies)

#11. Elimine la primera empresa informática de la lista.
del it_companies[0]
print(it_companies)

#12. Eliminar todas las empresas de TI de la lista.
it_companies.clear()
print(it_companies)