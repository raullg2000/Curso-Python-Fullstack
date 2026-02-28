import random

numero_secreto = random.randint(1, 9)
intentos = 0

print("--- 🔮 Adivina el número del 1 al 9 ---")

while True:
    entrada = input("Escribe un número (o 'exit' para salir): ").lower()
    
    if entrada == 'exit':
        print(f"Te has rendido. El número era el {numero_secreto}.")
        break
    
    intentos += 1
    
    if int(entrada) == numero_secreto:
        print(f"¡ENHORABUENA! 🎉 Lo has adivinado en {intentos} intentos.")
        break
    else:
        print("¡Error! Prueba otra vez.")