n = int(input("Ingrese un número: "))
impar = (n*(n-1)) + 1
acum = 0
for i in range(n):
    acum = acum + impar
    if 1 == (n-1):
       break
    impar = impar + 2
    print(impar)
print(f"El cubo de {n} es: {acum}")

n = int(input("Ingrese otro número: "))
impar = (n*(n-1)) + 1
acum = 0
for i in range(n):
    acum = acum + impar
    if 1 == (n-1):
       break
    impar = impar + 2
    print(impar)
print(f"El cubo de {n} es: {acum}")

n = int(input("Ingrese otro número más: "))
impar = (n*(n-1)) + 1
acum = 0
for i in range(n):
    acum = acum + impar
    if 1 == (n-1):
       break
    impar = impar + 2
    print(impar)
print(f"El cubo de {n} es: {acum}")

n = int(input("Ingrese otro y último número: "))
impar = (n*(n-1)) + 1
acum = 0
for i in range(n):
    acum = acum + impar
    if 1 == (n-1):
       break
    impar = impar + 2
    print(impar)
print(f"El cubo de {n} es: {acum}")