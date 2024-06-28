import os

Adivinar = int(input("Número a adivinar: "))
os.system("cls")

while True:
    Respuesta = int(input("Ingrese un número: "))
    if Respuesta == Adivinar:
        print(f"¡Adivinaste el número! Si era {Adivinar}")
        break
    elif Respuesta < Adivinar:
        print(f"Fallaste, el número es menor que {Adivinar}")
    elif Respuesta > Adivinar:
        print(f"Fallaste, el número es mayor que {Adivinar}")