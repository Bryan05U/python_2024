# Bucles While

# Llamando paquete colorama
from colorama import init, Fore

num = 0

print(Fore.CYAN + "Inicio de Ciclo N°1")
while num <= 100:
    print(num)
    #num = num + 2
    num += 2
print(Fore.CYAN + "Cierre de Ciclo N°1")

print(Fore.GREEN + "Inicio de Ciclo N°2")
while num <= 200:
    print(num)
    #num = num + 2
    num += 2
else:
    print(Fore.YELLOW + "La condición es igual o mayor a 200")
print(Fore.GREEN + "Cierre de Ciclo N°2")

print(Fore.CYAN + "Inicio de Ciclo N°3")
while num <= 300:
    print(num)
    num = num + 2
    if num == 250:
       print(Fore.RED + "Se detiene la ejecución")
       break
print(Fore.CYAN + "Cierre de Ciclo N°3")

# Ciclo For
print(Fore.YELLOW + "Inicio de Ciclo N°4 (FOR)")
nuevalist = [2,4,8,16,32,64,128,256,512,1024]
for i in nuevalist:
    print(i)

print(Fore.RED + "Inicio de Ciclo N°45 (FOR)")
for i in range(1,11):
    print(i)