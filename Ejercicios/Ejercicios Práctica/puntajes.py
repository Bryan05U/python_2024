matemáticas = (55, 17, 93, 75, 88, 55)
química = (10, 85, 75, 91, 75)
programación = (68, 78, 85, 68, 82, 10)

# A) Imprimir los valores duplicados de cada tupla.
materias = ["Matemáticas", "Química", "Programación"]
for i in range(len(materias)):
    asignaturas = materias[i]
    if asignaturas == "Matemáticas":
        puntajes = matemáticas
    elif asignaturas == "Química":
        puntajes = química
    elif asignaturas == "Programación":
        puntajes = programación

    duplicados = []
    for puntuación in puntajes:
        if puntajes.count(puntuación) > 1 and puntuación not in duplicados:
            duplicados.append(puntuación)

    print(f"Valores duplicados en Asignaturas {asignaturas}: tuple{duplicados}")

# B) Convertir cada tupla en una lista y ordenar las listas en orden descendente.
listaMatemáticas = list(sorted(matemáticas))
print(f"Puntajes de Matemáticas: {listaMatemáticas}")
listaQuímica = list(sorted(química))
print(f"Puntajes de Química: {listaQuímica}")
listaProgramación = list(sorted(programación))
print(f"Puntajes de Programación: {listaProgramación}")

# C) Unir las listas anteriormente generadas en una sola y eliminar los duplicados.
listaNueva = sorted(set(matemáticas + química + programación))
print(f"Nueva lista: {listaNueva}")

# D) Encontrar el puntaje máximo y mínimo de la lista resultante.
máximo = max(listaNueva)
print(f"Puntaje máximo: {máximo}")
mínimo = min(listaNueva)
print(f"Puntaje mínimo: {mínimo}")