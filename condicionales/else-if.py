ingreso_mensual = 100000
gasto_mensual = 1000000

#if anidado y else if (elif)
if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en deficit, debes plata bobo")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("estas bien")
    else:
        print("estas gastando una banda, hay que ver si te alcanza")
    
elif ingreso_mensual > 1000:
    print("estas bien economicamente en latinoamerica")
    
else:
    print("sos pobre")    
