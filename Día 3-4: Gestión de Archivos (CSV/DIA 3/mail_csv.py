import csv

def buscar_en_csv(nombre_buscado):
    try:
        with open('correos.csv', mode='r', encoding='utf-8') as fichero:
            lector = csv.reader(fichero)
            for fila in lector:
                # fila[0] es el Nombre, fila[1] es el Email
                if fila[0].strip().lower() == nombre_buscado.strip().lower():
                    return fila[1].strip()
        return None
    except FileNotFoundError:
        return "ERROR: No se encuentra el archivo 'correos.csv'."

nombre = input("Introduce el nombre para buscar en el CSV: ")
resultado = buscar_en_csv(nombre)

if resultado:
    print(f"📧 Email encontrado en el CSV: {resultado}")
else:
    print(f"⚠️ El nombre '{nombre}' no está en el archivo de correos.")