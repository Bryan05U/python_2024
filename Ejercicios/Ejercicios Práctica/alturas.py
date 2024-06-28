zona_central = (8848, 8611, 8586, 8200, 8460, 8200)
print(f"Zona Central: {zona_central}")
zona_sur = (8848, 5567, 8125, 4560, 8051, 4560)
print(f"Zona Sur: {zona_sur}")
zona_austral = (2200, 2500, 1000, 2200, 3623, 990)
print(f"Zona Austral: {zona_austral}")

# A) Imprimir los valores duplicados de cada tupla.
zonas = ["Central", "Sur", "Austral"]
for i in range(len(zonas)):
    zona = zonas[i]
    if zona == "Central":
        alturas = zona_central
    elif zona == "Sur":
        alturas = zona_sur
    elif zona == "Austral":
        alturas = zona_austral

# B) Verificar si la altura 8848m se encuentra en las tres tuplas utilizando bucles y condicionales.
    duplicados = []
    for altura in alturas:
        if alturas.count(altura) > 1 and altura not in duplicados:
            duplicados.append(altura)

    print(f"Valores duplicados en Zona {zona}: {tuple(duplicados)}")

datos = 8848 in zona_central and 8848 in zona_sur and 8848 in zona_austral
print(f"¿8848m está en las tres zonas?: {datos}")

# C) Unir las tuplas en una sola y eliminar los duplicados.
nuevatupla = tuple(set(zona_central + zona_sur + zona_austral))
print(f"Tupla sin duplicados: {nuevatupla}")

# D) Transformar la tupla obtenida en una lista. Imprimir la nueva lista obtenida.
nuevalista = list(nuevatupla)
print(f"Lista de alturas: {nuevalista}")