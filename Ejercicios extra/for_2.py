inicio = int(input("Ingrese el inicio del rango de numeros: "))
fin = int(input("Ingrese el fin del rango de numeros: "))
suma = 0

for num in range(inicio, fin + 1):
    if num % 2 == 0:
        suma += num
    
print ("la suma de los numeros pares es: ", suma)
    