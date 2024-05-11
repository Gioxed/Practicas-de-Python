#curso promedio dura 2,5hs minimo, 4hs promedio y 7hs maximo
#este curso en 1,5hs
#porcentaje entre el curso actual y el mas rapido de los otros cursos (2,5hs), el mas lento (7hs) y el promedio (4hs)
#otros cursos en crudo 5hs y lo reducen a 4hs
#crudo de este video 3,5hs reducido a 1,5hs
#calcular porcentaje de material inservible que se reduce en ambos casos
#ver 10 horas de este curso en cuanto equivale a otro curso y viceversa

otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4

curso_dalto = 1.5

crudo = 5
crudo_datlo = 3.5

diferencia_min = 100 - curso_dalto / otros_cursos_min * 100
diferencia_max = 100 - (curso_dalto * 1000 // otros_cursos_max /10)
diferencia_prom = 100 - (curso_dalto / otros_cursos_promedio * 100)

#calcular porcentaje removido de tiempo vacio
tiempo_promedio_vacio = 100 - otros_cursos_promedio * 1000 // crudo / 10
tiempo_dalto_vacio = 100 - curso_dalto * 1000 // crudo_datlo / 10

#diferencias
print("------------------")
print("diferencia de duración menos con el mínimo: ", diferencia_min, "%")
print("diferencia de duración menos con el máximo: ", diferencia_max, "%")
print("diferencia de duración menos con el promedio: ", diferencia_prom, "%")
print("------------------")

#vacios removidos
print("un curso promedio elimina un", tiempo_promedio_vacio, "% del tiempo vacio")
print("un curso de dalto elimina un", tiempo_dalto_vacio, "% del tiempo vacio")
print("------------------")

#diferencias de tiempo si los cursos duran 10hs
print("ver 10hs de este curso equivale a ver: ", otros_cursos_promedio *100 // curso_dalto / 10, "hs de otros cursos")
print("ver 10hs de otro curso equivale a ver: ", curso_dalto *100 // otros_cursos_promedio / 10, "hs de un curso de dalto")
print("------------------")
