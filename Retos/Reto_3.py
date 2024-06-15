"""
Crear dos listas que contengan la siguiente información:
● Ciudades: Santiago, Temuco, Osorno, Punta Arenas
● Índice de Calidad del Aire: 134, 99, 245, 50
Luego crear un algoritmo que imprima el nombre de la ciudad con el índice de calidad
del aire más bajo, y la ciudad con el índice de calidad del aire más alto.
Por último imprimir si ese índice, está dentro de que categoria:
● Buena: (ICA de 0 a 50)
● Moderada: (ICA de 51 a 100)
● Dañina a la salud para grupos sensibles: (ICA de 101 a 150)
● Dañina a la salud: (ICA 151 a 200)
● Muy dañina a la salud: (ICA 201 a 300)
● Peligrosa: (ICA superior a 300)
"""

print(f"######## LISTA DE CIUDADES #######")
ciudades = list(["Santiago", "Temuco", "Osorno", "Punta Arenas"])
print(ciudades)
print(f"######## LISTA DE ICA #######")
ica = [134, 99, 245, 50]
print(ica)

print(f"------------")
ica1 = 50
print(f"Ciudad con el índice de calidad del aire más bajo: {ciudades[3]}")
print(f"ICA: {ica1}")
if ica1 >= 0 and ica1 <= 50:
    print("Buena")
elif ica1 >= 51 and ica1 <= 100:
    print("Moderada")
elif ica1 >= 101 and ica1 <= 150:
    print("Dañina a la salud para grupos sensibles")
elif ica1 >= 151 and ica1 <= 200:
    print("Dañina a la salud")
elif ica1 >= 201 and ica1 <= 300:
    print("Muy dañina a la salud")
elif ica1 >= 300:
    print("Peligrosa")

print(f"------------")
ica2 = 245
print(f"Ciudad con el índice de calidad del aire más alto: {ciudades[2]}")
print(f"ICA: {ica2}")
if ica2 >= 0 and ica2 <= 50:
    print("Buena")
elif ica2 >= 51 and ica2 <= 100:
    print("Moderada")
elif ica2 >= 101 and ica2 <= 150:
    print("Dañina a la salud para grupos sensibles")
elif ica2 >= 151 and ica2 <= 200:
    print("Dañina a la salud")
elif ica2 >= 201 and ica2 <= 300:
    print("Muy dañina a la salud")
elif ica2 >= 300:
    print("Peligrosa")