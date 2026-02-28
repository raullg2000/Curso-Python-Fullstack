import sys
from datos_mail import directorio_emails

# sys.argv[0] es el nombre del script, sys.argv[1] sería el primer parámetro
if len(sys.argv) > 1:
    nombre = sys.argv[1]
    print(f"Consultando parámetro de consola: {nombre}")
else:
    nombre = input("Dime el nombre que quieres consultar: ")

# Buscamos en el diccionario
email = directorio_emails.get(nombre)

if email:
    print(f"El email de {nombre} es: {email}")
else:
    print(f"Lo siento, no tengo el email de {nombre}.")