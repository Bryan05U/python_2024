texto = input("Ingrese una cadena de texto: ").lower()

contador_a = 0; contador_e = 0; contador_i = 0; contador_o = 0; contador_u = 0

for letra in texto:
    if letra == 'a':
        contador_a = contador_a + 1
    elif letra == 'e':
        contador_e = contador_e + 1
    elif letra == 'i':
        contador_i = contador_i + 1
    elif letra == 'o':
        contador_o = contador_o + 1
    elif letra == 'u':
        contador_u = contador_u + 1
        
print(f"La letra 'a' aparece {contador_a} veces")
print(f"La letra 'e' aparece {contador_e} veces")
print(f"La letra 'i' aparece {contador_i} veces")
print(f"La letra 'o' aparece {contador_o} veces")
print(f"La letra 'u' aparece {contador_u} veces")