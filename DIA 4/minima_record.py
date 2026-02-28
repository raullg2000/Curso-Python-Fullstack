import csv

# 1. Mapeo de nombres de estaciones
estaciones = {}
with open('estaciones.csv', mode='r', encoding='utf-8') as f:
    lector = csv.DictReader(f)
    for fila in lector:
        estaciones[fila['CODI_ESTACIO']] = fila['NOM_ESTACIO']

# 2. Encontrar la temperatura más baja de todo el archivo
temp_minima_absoluta = float('inf') # Empezamos con un número infinito
registros_minimos = []

with open('temperaturas.csv', mode='r', encoding='utf-8') as f:
    lector = csv.DictReader(f)
    for fila in lector:
        if fila['ACRÒNIM'] == 'TN':
            valor_actual = float(fila['VALOR'])
            
            # Si encontramos un nuevo récord de frío
            if valor_actual < temp_minima_absoluta:
                temp_minima_absoluta = valor_actual
                # Limpiamos la lista porque hay un nuevo récord
                registros_minimos = [fila]
            # Si se repite la misma temperatura mínima, la añadimos
            elif valor_actual == temp_minima_absoluta:
                registros_minimos.append(fila)

# 3. Mostrar el resultado final
print(f"🌡️ LA TEMPERATURA MÍNIMA HA SIDO: {temp_minima_absoluta}ºC")
print("-" * 60)
print(f"{'DATA-HORA':<25} | {'ESTACIÓ'}")
print("-" * 60)

for reg in registros_minimos:
    nom = estaciones.get(reg['CODI_ESTACIO'], "Desconeguda")
    fecha_completa = f"{reg['DATA_LECTURA']} {reg['DATA_EXTREM']}"
    print(f"{fecha_completa:<25} | {nom}")