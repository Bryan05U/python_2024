"""
Obtener los números del rango 10 al 50, incrementando de 2 en 2.
A continuación, sumar todos los números obtenidos.
"""
print(f"##### Rango del 10 al 50 #####")
num = 10
while num <= 50:
    print(num)
    num = num + 2

total = sum(i for i in range(10,51,2))
print(f"Suma total del rango del 10 al 50: ", total)