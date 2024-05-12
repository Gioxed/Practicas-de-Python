lista = [0, 1, 24, 3, 4]
indice1 = 1
indice2 = 3

if indice1 < 0 or indice2 < 0:
    print("Error, el índice no puede ser menor que 0")
elif indice1 > len(lista) or indice2 > len(lista):
    print("Error, el índice no puede ser mayor a la longitud de la lista")
else:
    num1 = lista[indice1]
    num2 = lista[indice2]  
    suma = num1 + num2
    print("La suma es:", suma)

# print ("ingrese valores a la lista")
# int(input(lista.extend))