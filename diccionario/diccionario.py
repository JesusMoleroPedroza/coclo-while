#1
perro = {}
print(perro)
print()

#2
perro['nombre'] ='luna'
perro['color'] ='marron'
perro['raza']='bulldog'
perro['patas']='4'
perro['edad']='2 años'
print(perro)
print()

#3
estudiantes={}
estudiantes['nombre']='jesús'
estudiantes['apellido']='molero'
estudiantes['sexo']='masculino'
estudiantes['edad']=20
estudiantes['estado_civil']='soltero'
estudiantes['habilidades']=['programar php','programar python']
estudiantes['pais']='colombia'
estudiantes['ciudad']='cartagena'
estudiantes['direccion']='bayunca'
print(estudiantes)
print()

#4
print('tamaño de la lista',estudiantes.__len__())
print()

#5
print('habilidades:',estudiantes['habilidades'])
print('tipo de dato:',type(estudiantes['habilidades']))
print()

#6
estudiantes['habilidades'].append('programar c++')
print('modificacion:',estudiantes['habilidades'])
print()

#7
llaves=estudiantes.keys()
print(llaves)
print()

#8
valores=estudiantes.values()
print(valores)
print()

#9
print(estudiantes.items())
print()

#10
estudiantes.pop('direccion')
print(estudiantes)
print()

#11
del perro
