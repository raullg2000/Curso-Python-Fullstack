import csv

# 1. Mapeig de codis a noms d'estacions
estacions = {}

try:
    # Llegim les metadades de les estacions
    with open('estaciones.csv', mode='r', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        for fila in lector:
            # Usem el nom exacte de la columna: CODI_ESTACIO i NOM_ESTACIO
            estacions[fila['CODI_ESTACIO']] = fila['NOM_ESTACIO']

    print(f"{'DATA-HORA':<20} | {'MÍNIMA (TN)':<12} | {'ESTACIÓ'}")
    print("-" * 70)

    # 2. Llegim les temperatures
    with open('temperaturas.csv', mode='r', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        for fila in lector:
            # ATENCIÓ: 'ACRÒNIM' amb accent tal com surt al teu fitxer
            if fila['ACRÒNIM'] == 'TN':
                data = fila['DATA_LECTURA']
                hora = fila['DATA_EXTREM']
                valor = fila['VALOR']
                codi_est = fila['CODI_ESTACIO']
                
                # Obtenim el nom de l'estació del nostre diccionari
                nom_estacio = estacions.get(codi_est, "Desconeguda")
                
                # Combinem data i hora per al llistat
                data_hora = f"{data} {hora}"
                
                print(f"{data_hora:<20} | {valor:<12} | {nom_estacio}")

except KeyError as e:
    print(f"❌ Error: No s'ha trobat la columna {e}. Revisa els accents (ex: ACRÒNIM).")
except FileNotFoundError:
    print("❌ Error: No s'han trobat els fitxers .csv a la carpeta actual.")