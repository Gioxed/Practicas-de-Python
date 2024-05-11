#creando una lista con List()
lista = list([0, False, 32, 56, 18])

#devuelve la cantidad de elementos de una lista
cantidad_elementos = len(lista)

#agregar un elemento a la lista
agregando_con_append = lista.append(65)

#agregar un elemento a la lista en un índice específico
lista.insert(2, "TOMA")

#agregando varios elementos a la lista
lista.extend([True, 2030])

#eliminando un elemento de la lista por su indice
lista.pop(0) #-1 para eliminar el ultimo elemento, -2 para eliminar el anteultimo

#removiendo un elemento de la lista por su valor
lista.remove("TOMA")

#ordena los elementos de forma ascendente, solo valido para números y bool
lista.sort()
#ordenando la lista si usamos el parametro reverse=true (ordena los elementos al reves)
lista.sort(reverse=True)

#invirtiendo los elementos de una lista, no ordenadamente
lista.reverse()

#eliminando todos los elementos de la lista
lista.clear()

print(lista)

