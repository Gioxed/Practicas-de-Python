#creando diccionarios con dict()
diccionario = dict(nombre = "Gio", apellido = "Pauletto")

#las listas no pueden ser claves y usamos prozenset para meter conjuntos
diccionario = {frozenset(["Gio"]): "hola"}
#tupla:
diccionario = {("Gio", "Hola"): "jajas"}

#creando diccionarios con fromkeys() con dos parametros
#primer dato un iterable, segundo dato lo que vamos a igualar
dicc = dict.fromkeys("ABC", "Hola")

#valor por defecto: None
diccionario = dict.fromkeys(["nombre", "apellido"])

print(diccionario)
print(dicc)