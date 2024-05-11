Material_total = 100 

while True: 

    opcion = int(input("""¿Qué necesitas hacer? Elige una opción numérica:
    1 = Consumir
    2 = Cargar
    3 = Consultar
    4 = Salir
    """))

    if opcion == 1:
        consumir = int(input("¿Cuánto material se consumió? en paladas: "))
        Material_total -= consumir 
        print("El material actual es: ", Material_total)
    elif opcion == 2:
        cargar = int(input("¿Cuánto material se cargó? en paladas: "))
        Material_total += cargar
        print("El material actual es: ", Material_total)
    elif opcion == 3:
        print("La cantidad del material restante es: ", Material_total)
    elif opcion == 4:
        print("Salir del programa")
        break 

    else:
        print("La opción no corresponde")

