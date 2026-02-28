import sys
from datos_mail import buscar_email

# Si el usuario pone: python3 mail_v2.py JuanMiguel
if len(sys.argv) > 1:
    nombre = sys.argv[1]
else:
    nombre = input("Dime el nombre a consultar en el diccionario: ")

try:
    email = buscar_email(nombre)
    print(f"✅ Encontrado: {email}")
except KeyError as e:
    print(f"❌ Error: {e}")