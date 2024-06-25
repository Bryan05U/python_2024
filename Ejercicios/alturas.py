zona_central = ("8848","8611","8586","8200","8460","8200")
zona_sur = ("8848","5567","8125","4560","8051","4560")
zona_austral = ("2200","2500","1000","2200","3623","990")

print(f"Alturas en la Zona Central: {zona_central}")
print(f"Alturas en la Zona Sur: {zona_sur}")
print(f"Alturas en la Zona Austral: {zona_austral}")
print(f"Valores duplicados (8200): ", zona_central.count("8200"))
print(f"Valores duplicados (4560): ", zona_sur.count("4560"))
print(f"Valores duplicados (2200): ", zona_austral.count("2200"))

datos = 8848 in zona_central and 8848 in zona_sur and 8848 in zona_austral
print(f"¿8848m está en las tres zonas?: {datos}")

todas = set(zona_central), set(zona_sur), set(zona_austral)
print(todas)