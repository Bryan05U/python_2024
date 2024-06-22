H = 0; M = 0; S = 0

print("Ingrese la hora actual")
H = int(input("Hora: "))
M = int(input("Minutos: "))
S = int(input("Segundos: "))

while H < 24:
    while M < 60:
        while S < 60:
            print(H, ":", M, ":", S)
            S = S + 1
        M = M + 1
        S = 0
    H = H + 1
    M = 0