diccionario = {
    "nombre": "Gio",
    "apellido": "Pauletto",
    "edad": 18
}

#recorrer un diccionario para obtener las clave
for key in diccionario:
    print("la clave es:", key)

#recorrer un diccionario con items() para obtener las clave y los valores
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print("la clave es:", key, "y el valor es:", value)

