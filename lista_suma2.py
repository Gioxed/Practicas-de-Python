lista = [0, 1, 24, 3, 4] #lista de números
indice = 1 #indice donde se va a almacenar el valor numérico de la lista

if indice < 0: #si el número del indice es menor que cero (ejemplo: -1)
    print("Error, el índice no puede ser menor que 0") #imprime un error
elif indice >= len(lista): #si el número del indice supera la longitud de la lista
    print("Error, el índice no puede ser mayor a la longitud de la lista") #imprime un error

else:
    num1 = lista[indice]  #guarda en una variable el número del índice
    num2 = lista[indice]  

#suma los números e imprime el resulado
suma = num1 + num2
print("La suma es:", suma)





#ver si se puede hacer a traves de un bucle ir agregando valores para despues sumarlos 