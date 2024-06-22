n = int(input("Ingrese un número: "))

def número_factorial(n):
    if n == 0:
        return 1
    else:
        return n * número_factorial(n-1)
    
print("La factorial es :", número_factorial(n))