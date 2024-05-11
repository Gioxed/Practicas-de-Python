lista = [100, 56, 17, 79, 9, 8, 120]

mayor = lista[0]
menor = lista[0]

for n in lista:
    
    if n > mayor:
        mayor = n
    if n < menor:
        menor = n
        
print("el mayor numero es: ", mayor)
print("el menor numero es: ", menor)