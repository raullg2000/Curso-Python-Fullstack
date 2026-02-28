num = int(input("Introduce un número: "))
divisor = int(input("Introduce otro número para comprobar divisibilidad: "))

if num % divisor == 0:
    print(f"El {num} es divisible por {divisor}.")
elif num % 4 == 0:
    print(f"El {num} es múltiplo de 4 (y por tanto par).")
elif num % 2 == 0:
    print(f"El {num} es un número par.")
else:
    print(f"El {num} es un número impar.")