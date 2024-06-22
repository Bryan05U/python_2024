n1 = 500
n2 = 456
S = 0

while n1 != 800:
    S = S + n1
    S = S + n2
    n1 = n1 + 10
    n2 = n2 - 2
    S = S + 800
print(f"La sumatoria de 500 + 456 + 510 + 454 + 520 + 452 + ... + 800 es: {S}")