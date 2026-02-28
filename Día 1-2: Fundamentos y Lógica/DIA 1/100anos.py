from datetime import datetime

nombre = input("Dime tu nombre: ")
edad = int(input("¿Cuántos años tienes?: "))
año_actual = datetime.now().year

if edad >= 100:
    print(f"¡Increíble {nombre}! Ya eres centenario.")
else:
    faltan = 100 - edad
    año_100 = año_actual + faltan
    print(f"Hola {nombre}, cumplirás los 100 años en el año {año_100}.")