#Este es un Hola Mundo
print("Hola Mundo!");

"""Este es un
comentario multilinea"""




# 1. Declaración de Variables
nombre = "Bryan"
apellido = "Cárcamo"
edad = 18 
pi = 3.14

# 2. Impresión de Variable (Print Clásico)
print("Hola soy", nombre)

# 3. Impresión de Variable (Cadenas Literales - f-string)
print(f"Hola mi nombre es {nombre} y tengo {edad}")

# 4. Impresión de Variable (Concatenación)
print("Hola mi nombre es " + nombre + " " + apellido + " y tengo " + str(edad) + " años")

# 5. Declarando Variables Numéricas
estatura = 1.75 #declarando número real
n_comp = 5 + 4j
n_comp2 = complex(5,4)

#Formatos de Salida Númerica (Flotantes)
print("PI: ", round(pi,4)) #Ocupando función Round
print(f"PI: {pi:.2f}") #Ocupando formato con f-string

# 7. Variables en una sola linea

país, región, ciudad, código_postal = "Chile", "Los Lagos", "Coinco", 30100000
print(país + región + ciudad + str(código_postal))

# 8. Utilizando Input

año = input("En qué año naciste")
print("Nací en el año: " + año)
