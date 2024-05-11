diccionario = {
    "nombre":"Gio",
    "apellido":"pauletto",
    "edad":18
}

#devuelve un objeto dict_item
claves = diccionario.keys()

#obteniendo un elemento con get, no salta error si no encuentra el valor, salta none y el programa continua
valor = diccionario.get("nombre")

#eliminando un elemento del diccionario
diccionario.pop("nombre")

#obteniendo un elemento dict_items iterable
item = diccionario.items()

#eliminando todo del diccionario
#diccionario.clear()

print(item)