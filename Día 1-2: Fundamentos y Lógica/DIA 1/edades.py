from datetime import datetime

nacimientos = [2000, 1995, 2005, 1988, 2002]
año_actual = datetime.now().year

edades = []
for año in nacimientos:
    edades.append(año_actual - año)

print(f"Años de nacimiento: {nacimientos}")
print(f"Lista de edades calculadas: {edades}")