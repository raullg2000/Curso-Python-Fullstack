palabra = input("Introduce una palabra: ").lower()

# 
# El truco [::-1] invierte la cadena en Python
if palabra == palabra[::-1]:
    print(f"¡Sí! '{palabra}' es un palíndromo.")
else:
    print(f"No, '{palabra}' no es un palíndromo.")