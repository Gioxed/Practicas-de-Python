texto = input("ingrese una oración: ")
vocales = 0
texto = texto.lower()

for a in texto:
    if a in ("a", "e", "i", "o", "u"): 
        vocales += 1
    
print("la cantidad de vocales es: ", vocales)