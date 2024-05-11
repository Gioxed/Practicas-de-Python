# ID: ["Persona", "Cargadora", "Pala"]
Material_actual = int(input("Ingrese la cantidad del material actual en paladas: "))
Paladas = 30

if Material_actual < Paladas:
    print("La cantidad de material es menor a la cantidad de paladas")
elif Material_actual > Paladas: 
    Material_consumido = Paladas
    Material_total = Material_actual - Paladas

print("La cantidad del material restante es: ", Material_total)
print("La cantidad del material consumido es: ", Material_consumido)
