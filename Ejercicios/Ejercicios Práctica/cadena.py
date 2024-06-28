cadena = input("Ingrese una cadena de texto: ")

cadena_invertida = ""

for carácter in cadena:
    cadena_invertida = carácter + cadena_invertida

print(f"Cadena invertida: {cadena_invertida}")