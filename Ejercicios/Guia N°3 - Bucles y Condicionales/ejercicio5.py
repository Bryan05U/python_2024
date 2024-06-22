"""
5. Crear 20 números, que se encuentren en el intervalo 40 al 350 y los almacene en una
lista y luego pida buscar algun número dentro de los almacenados. Además que muestre
la cantidad de ocurrencias de ese número buscado. (Se permite el uso de la Biblioteca
Random)
"""

intervalo = True

while intervalo:
    n = int(input("Número entero entre el 40 y el 350: "))
    if n in range(40,350):
        print("Dentro del rango")
    else:
        print("Fuera del rango")
        intervalo = False