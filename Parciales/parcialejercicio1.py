TempMin = (9, 5, 2, 7, 6, 1)
TempMax = (12, 14, 11, 10, 15, 9)

# A) Verificar si la temperatura 9°C se encuentra en ambos sets utilizando condicionales.
Verify = True
if 9 in TempMin and TempMax:
    print(f"¿La temperatura 9°C se encuentra en ambos sets?: {Verify}")

# B) Unir ambos sets en un solo y eliminar duplicados. Imprimir el set generado.
NewSet = set(TempMin + TempMax)
print(f"Nuevo set: {NewSet}")

# C) Transformar el set en una lista, y encontrar las temperatura mínima y máxima utilizando bucles. Imprimir los resultados.
NewLista = list(NewSet)
print(f"Set a lista: {NewLista}")
Min = min(NewLista)
Max = max(NewLista)
print(f"Temperatura mínima: {Min}")
print(f"Temperatura máxima: {Max}")

# D) Crear una tupla con los valores de temperaturas mínima y máxima, más un string con las etiquetas de texto: “Mínima” y “Máxima”. Imprimir la tupla generada.
NewTupla = str(f"Mínimo: {tuple[Min]}"), str(f"Mínimo: {tuple[Max]}")
print(f"Tupla con los valores: {NewTupla}")

# E) Generar e imprimir un diccionario donde las claves sean las temperaturas y los valores sean la frecuencia de aparición.
Temperaturas = dict(
    Temperaturas = NewLista,
    Temperatura_Mínima = Min,
    Temperatura_Máxima = Max
)
print(f"Diccionario: {Temperaturas}")