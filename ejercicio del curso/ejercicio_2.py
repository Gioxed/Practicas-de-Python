#si en 1 segundo una persona puede decir dos palabras...
#pedirle a un usuario una frase y calcular cuanto tardaría en decirla, cuantas palabras dijo?
#si tarda más de un minuto decirle "pará flaco, tampoco te pedí un testamento"
#cuanto tardaría dalto en decirlo teniendo en cuenta que habla un 30% más rápido?
print("calculadora de cuanto tardarías en decir una frase :O")
frase = input("escriba una frase: ")

palabras = frase.split(" ")
cantidad = len(palabras)
if cantidad > 10:
    print("para flaco, tampoco te pedí un testamento")
    
print("dijiste", cantidad, "palabras y tardarías en decirla unos", cantidad/2, "segundos")
print("dalto lo diría en: ", cantidad* 100 //2*0.7 /100, "segundos")


