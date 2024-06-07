# 1. Creando una descripción
descripción = "Este bolígrafo es multicolor"

# 2. Se muestra los primeros 50 carácteres si excede esa longitud se trunca la cadena
descripción = descripción[:50]

# 3. Se verifica si la longitud supera a 50 carácteres
longitud = len(descripción) > 50 # Booleano (Se determina si la longitud es True o False)
print(type(longitud))

# 4. Mostrar los 10 primeros carácteres de la descripción
desc_10 = descripción[:10]

print(f"\nDescripción: {descripción}")
print(f"¿El tamaño de la cadena descripción es superior a 50 caracteres? {longitud}")
print(f"Los primeros 10 carácteres de la descripción: {desc_10}")