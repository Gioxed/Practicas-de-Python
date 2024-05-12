animales = ["perro", "gato", "loro", "cocodrilo"]
numeros = [10, 20, 30, 40]

#recorriendo la lista animales
for animal in animales:
    print("ahora la variable animal es igual a: ", animal)
    
#multiplicar los numeros de la lista * 10
for numero in numeros:
    resultado = numero * 10
    print(resultado)
    
#iterando dos listas del mismo tamaño al mismo tiempo intercalando
for numero, animal in zip(animales, numeros):
    print("recorriendo lista 1:", numero)
    print("recorriendo lista 2:", animal)
    
for num in range(5, 10):
    print(num)
    
#forma no oprima de recorrer una lista con su indice
for num in range(len(numeros)):
    print(numeros[num])
    
#forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el indice es: {indice} y el valor es: {valor}")