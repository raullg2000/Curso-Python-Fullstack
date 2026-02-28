jugador1 = input("Nombre del Jugador 1: ")
jugador2 = input("Nombre del Jugador 2: ")

while True:
    print("\n--- Nueva Partida (escribe 'salir' para terminar) ---")
    p1 = input(f"{jugador1}, ¿piedra, papel o tijera?: ").lower()
    if p1 == "salir": break
    
    p2 = input(f"{jugador2}, ¿piedra, papel o tijera?: ").lower()
    if p2 == "salir": break

    if p1 == p2:
        print("¡Empate!")
    elif (p1 == "piedra" and p2 == "tijera") or \
         (p1 == "tijera" and p2 == "papel") or \
         (p1 == "papel" and p2 == "piedra"):
        print(f"¡Gana {jugador1}!")
    else:
        print(f"¡Gana {jugador2}!")