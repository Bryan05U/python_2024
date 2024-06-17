"""
Crear un algoritmo capaz de generar la series de Fibonacci basadas en
un valor n ingresado por teclado. Solamente utilizando bucles.
"""

n = int(input(f"Ingrese n: "))
while n <= 1000:
    print(n)
    n = (n + 1) + (n + 2)