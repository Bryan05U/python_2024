"""Objetivo
Crear un algoritmo que permita ingresar y gestionar las notas de un estudiante en tres asignaturas diferentes,
utilizando diccionarios, tuplas, sets y listas. El algoritmo debe calcular el promedio final ponderado de cada
estudiante por asignatura y mostrar toda la información ingresada.
Instrucciones:
1. Entrada de Datos:
● Nombre del estudiante.
● Nombre de la asignatura.
● Nota del Laboratorio N°1.
● Nota del Laboratorio N°2.
● Nota del Laboratorio N°2.
2. Estructuras de Datos Utilizadas:
● Utilizar un diccionario para almacenar la información de un solo estudiante.
● La clave del diccionario es el nombre del estudiante.
● El valor asociado a la clave es una lista de tuplas, donde cada tupla contiene:
   ○ Nombre de la asignatura.
   ○ Un set con las dos notas de laboratorio.
   ○ El promedio final ponderado calculado.
3. Operaciones Matemáticas:
● La ponderación del Laboratorio N°1 es de un 30% del promedio final.
● La ponderación del Laboratorio N°2 es de un 50% del promedio final.
● La ponderación del Laboratorio N°3 es de un 20% del promedio final.
● El promedio final debe mostrarse con un punto flotante de máximo 1 decimal.
 4. Salida de Datos:
● Mostrar toda la información ingresada junto con el promedio final ponderado."""

import math

nombre_estudiante = str(input("Ingrese el nombre del estudiante: "))
asignatura_1 = str(input("Ingrese el nombre de la primera asignatura: "))
asig1notalab_1 = 4.3
asig1notalab_2 = 5.0
asig1notalab_3 = 5.5

asignatura_2 = str(input("Ingrese el nombre de la segunda asignatura: "))
asig2notalab_1 = 5.2
asig2notalab_2 = 6.7
asig2notalab_3 = 3.1

asignatura_3 = str(input("Ingrese el nombre de la tercera asignatura: "))
asig3notalab_1 = 3.4
asig3notalab_2 = 2.7
asig3notalab_3 = 7.0

nombre_estudiante = [asignatura_1, asignatura_2, asignatura_3]
print(nombre_estudiante)
notasasig1 = [asig1notalab_1, asig1notalab_2, asig1notalab_3]
print(f"Notas de la primera asignatura: ",notasasig1)
notasasig2 = [asig2notalab_1, asig2notalab_2,asig2notalab_3]
print(f"Notas de la segunda asignatura: ", notasasig2)
notasasig3 = [asig3notalab_1, asig3notalab_2,asig3notalab_3]
print(f"Notas de la tercera asignatura: ", notasasig3)