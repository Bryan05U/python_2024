"""
Crear un algoritmo capaz de generar la series de Fibonacci basadas en
un valor n ingresado por teclado. Solamente utilizando bucles.
"""
n = int(input("Ingrese el número de la serie de Fibonacci para la impresión de la serie: "))
a = 0
b = 1

fibonacci = [a, b]

while True:
    c = a + b
    if c > n:
        break
    fibonacci.append(c)
    a = b
    b = c

    # a, b = b, c

print(" ".join(map(str, fibonacci)))