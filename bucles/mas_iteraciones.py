
frutas = ["banana", "manzana", "ciruela", "pera", "naranja", "granada", "durazno"]
cadena = "hola xd"
numeros = [2, 5, 8, 10]

#evitando que se coma una granada con la sentencia continue
for fruta in frutas:
    if fruta == "granada":
        continue
    print("me voy a comer una", fruta)

#evitar que el bucle siga ejecutandose (el else no se ejecuta tampoco)
for fruta in frutas:
    print("me voy a comer una", fruta)
    if fruta == "pera":
        break
else:
    print("bucle terminado")

#recorrer una cadena
for letra in cadena:
    print(letra)


#for en una sola línea de código (duplicamos los numeros)
numeros_duplicados = [x*2 for x in numeros]
#forma larga:
# numeros_duplicados = list()
# for numero in numeros:
#     numeros_duplicados.append(numero*2)

print(numeros_duplicados)