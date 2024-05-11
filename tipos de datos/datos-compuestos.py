#creando una lista (se puede modificar)
lista = ["Giovanni Pauletto", 18, 165, True]

#creando una tupla (no se puede modificar)
tupla = ("Giovanni Pauletto", 18, 165, True)

#esto es valido
lista[1] = 20

#esto no es valido
#tupla[2] = 160

#creando un conjunto (set)
conjunto = {"Giovanni Pauletto", 18, 165, True}
#print (conjunto[2]) = no puede acceder al elemento

#creando un diccionario (dict)
diccionario = {
    'nombre' : 'Gio',
    'Esta_emocionado' : True,
    'Edad' : 18,
    'Valor_duplicado' : 'Gio'
}
print(diccionario['Edad'])

