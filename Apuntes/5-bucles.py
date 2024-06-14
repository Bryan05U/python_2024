# Bucles While

# Llamando paquete colorama
from colorama import init, Fore

num = 0

print(Fore.CYAN + "Inicio Ciclo N°1")
while num <= 100:
    print(num)
    #num = num + 5
    num += 5
print(Fore.CYAN + "Fin Ciclo N°1")

print(Fore.GREEN + "Inicio Ciclo N°2")
while num <= 200:
    print(num)
    #num = num + 5
    num += 5
else:
    print(Fore.YELLOW + "La condición es igual o mayor a 200")
print(Fore.GREEN + "Fin Ciclo N°2")
