# Entrada de datos: edad de la persona
# Tiene que existir 5 categorías para determinar a cuál pertenece la persona

"""
   Edad inválida < 0
   Niño/a <= 12
   Adolescente <= 17
   Adulto/a <= 64
   Adulto/a mayor >= 120
"""

edad = int(input("Ingrese la edad de la persona: "))
if edad < 0 or edad >= 120:
    categoría = "Edad inválida"
elif edad <= 12:
    categoría = "Niño/a"
elif edad <= 17:
    categoría = "Adolescente"
elif edad <= 64:
    categoría = "Adulto/a"
else:
    categoría = "Adulto/a mayor"
print(f"La persona es: {categoría}")