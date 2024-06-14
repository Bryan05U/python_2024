import math

# 1. Números
estatura = 1.75
peso = 90

# 2. Potencia
imc = peso / (estatura ** 2)
print(imc)
print(math.trunc(imc))

# 3. Strings
institución = "Ulagos"
asignatura = 'Programación'
descripción = """Asignatura de 1er semestre de la carrera de Ingeniería Civil en Informática"""

# 4. Imprimir la posición de un carácter
print(institución[-1])

# 5. Concatenación
resultado = print(institución + " " + asignatura)

# 6. Multiplicación
salida = print(institución * 4)

# 7. Utilizando la función splint en strings
print(institución.split())
print(len(institución))

# 8. Declarando e inicializando listas
ciudades = ["Coinco", "Castro", "Ancud", "Quellón", "Chonchi", "Coinco", "Queilen"]
print(ciudades)
print(type(ciudades))
print(len(ciudades)) # Contador de elementos de una lista
print(ciudades.count("Coinco")) # Contador de ocurrencia de

# 9. Impresión de un elemento en específico de la lista
print(ciudades[2])

# 10. Lista de los diez primeros números
listnum = [1,2,3,4,5,6,7,8,9,10]
listnum2 = list(range(10)) # Función de rango
print(listnum) # Impresión normal
print(listnum2) # Impresión con range

# 11. Tuplas
música = tuple()
estilos = ("New Wave", "Punk", "Indie")
print(estilos)
print(type(estilos))
print(estilos[2])
print(estilos.index("Indie"))

