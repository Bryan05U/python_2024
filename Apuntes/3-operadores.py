# 1. Operadores aritméticos

# Declarando variables de tipo entero
a = 12
b = 10
c = 18
d = 15

# Operaciones comúnes
print("########## 1. Operadores aritméticos ##########")
print("Suma entre a + b es: ",a + b)
print("Resta entre a - b es: ",a - b)
print("Multiplicación entre a * b es: ",a * b)
print("División entre a / b es: ",a / b)
print("El módulo entre a y b es: ",a % b)
print("El cociente entre b / c es:",b // c)
print("El resultado de b elevado a c (5^4):",b ** c,"\n")

# Declarando variables de tipo flotantes
p = 3.25 # Tiempo en segundos
y = 7.78 # La aceleración de gravedad

# Operaciones artiméticas con flotantes
v = y * p

print(f"La velocidad del objeto en caída libre es de: {v} m/s")
print("La velocidad del objeto en caída libre es de: {:.2f}".format(v)) # Primera manera de formatear decimales
print(f"La velocidad del objeto en caída libre es de: {v:.2f}") # Segunda manera de formatear decimales con f-string
print("La velocidad del objeto en caída libre es de: ","%.2f" % v) # Utilizando el formateador %f
print("\n")

# Declarando variables de tipo compleja
c1 = 9 + 9j
print(type(c1))

# Creando un número complejo con complex
c2 = complex(-6, 3)
print("El número complejo es: ",c2)
print(c2.real) # Obteniendo la parte real del número complejo
print(c2.imag) # Obteniendo la parte imaginaria del número complejo

# ¿Se puede realizar esta operación? ¿Multiplicar un String por un entero?
print("Python" * 5)
# ¿Y la siguiente multiplicación?
# print("Python * 3.5*2")
# Si el resultado es un 7 (número entero), ¿por qué sale error?

# ¿Qué tal con esta operación un poco más elaborada?
print("Python" * (int((10 * 2) / 5)),"\n")
# ¿Y por último esta operación de suma?
# print ("Python" + 20)

# 2. Operaciones de comparación
print("########## 2. Operadores de comparación ##########")
print(a == b) # Igual a
print(a != b) # Desigual a
print(a > b) # Mayor que
print(a < b) # Menor que
print(c >= d) # Mayor o igual a
print(c <= d) # Menor o igual a

# Comparando cadenas de carácteres
fruta_1 = "Pera"
fruta_2 = "Manzana"
print("\nComparando cadenas de carácteres")
print(fruta_1 == fruta_2) # Igual a
print(fruta_1 != fruta_2) # Desigual a
print(fruta_1 > fruta_2) # Mayor que
print(fruta_1 < fruta_2) # Menor que
print(fruta_1 >= fruta_2) # Mayor o igual a
print(fruta_1 <= fruta_2) # Menor o igual a

# 3. Operaciones lógicos
print("########## Operaciones lógicos ##########")
print("--- Método If ---")
edad = 19
print(f"Si tu edad es: {edad}")
if edad >= 18:
    print("Eres mayor de edad")

print("--- Método Else ---")
edad = 17
print(f"Al contrario si es: {edad}")
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print("--- Método Elif ---")
edad = 68
print(f"Si tu edad es: {edad}")
if edad >= 18 and edad < 65:
    print("Eres mayor de edad")
elif edad >= 65:
    print("Eres un adulto mayor")
else:
    print("Eres menor de edad")

print("--- Operadores ternarios ---")
edad = 19
print(f"Si tu edad es: {edad}")
print("Usted podrá votar" if edad >= 18 else "Usted no podrá votar")