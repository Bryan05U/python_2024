import numpy as np
import pandas as pd

def saludo():
    print("Hola mi nombre es Bryan")
saludo()

def funcion(x):
    return x * 15
y = funcion(30)
print(f"El resultado de la función es {y}")

def saludo(nombre):
    print(f"Hola mi nombre es {nombre}")
saludo("Bryan")