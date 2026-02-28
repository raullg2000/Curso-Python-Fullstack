lista_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lista_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

comunes = []
for x in lista_a:
    if x in lista_b and x not in comunes:
        comunes.append(x)

print(f"Los números que aparecen en ambas listas son: {comunes}")