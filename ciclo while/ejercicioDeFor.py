Vuelo = {
    'Aerolinea': 'Avianca',
    'Vuelo': 'AV3102',
    'Origen': 'CTG',
    'Destino': 'MDE',
    'Tipo_Maleta': ['Cabina', 'Mano', 'Bodega']
}


print("Los valores del diccionario Vuelo son:")
for key, value in Vuelo.items():
    print(key + ":", value)
print("\n")
print("Valores de tipo de maleta:")
for tipo_maleta in Vuelo['Tipo_Maleta']:
    print(tipo_maleta)
