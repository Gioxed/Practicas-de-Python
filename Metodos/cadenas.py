cadena1 = "Hola soy Gio"

#convierte a minúsculas
minusc = cadena1.lower()

#resultado = (dir(cadena1)) / primera letra en mayúscula
resultado = cadena1.capitalize()

#buscamos una cadena en otra cadena, si no hay coincidencias devuelve -1
busq_find = cadena1.find("g")

#lo mismo pero sinó lanza error
busq_index = cadena1.index("o")

#si es numérico devuelve true, sino es false
numerico = cadena1.isnumeric()

#si es alfanumérico devuelve true, sino es false/ los espacios son caracteres especiales
alpha = cadena1.isalpha()

#cuenta las coincidencias en la cadena, devuelve la cantidad de veces que coincida.
coincid = cadena1.count("o")

#contamos cuantos caracteres tiene una cadena
contar = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es así, devuelve true
empieza_con = cadena1.startswith("H")

#verificamos si una cadena termina con otra cadena dada, si es así, devuelve true
termina_con = cadena1.endswith("o")

#reemplaza un pedazo de la cadena por otra solosi se encuentra en la original
nueva = cadena1.replace("la", "liwis xd")

#separar cadenas con la cadena que le pasemos
separada = cadena1.split(" ")

print(separada)
