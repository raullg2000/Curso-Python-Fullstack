# Diccionario con al menos 10 registros
directorio_emails = {
    "JuanMiguel": "juanmiguel301205@gmail.com",
    "Óscar": "oducuara12@gmail.com",
    "Lluc": "llukflores10@gmail.com",
    "Hans": "jami2710.39@gmail.com",
    "Gerard": "gerard.gonzalez0312@gmail.com",
    "Raúl": "ralugo00@gmail.com",
    "Cristian": "cristianxx14@gmail.com",
    "Diego": "dmiguelgaliana@gmail.com",
    "Sergio": "srms1866@gmail.com",
    "Jaume": "jaumemd161718@gmail.com"
}

def buscar_email(nombre):
    """Busca un nombre en el diccionario y devuelve el mail o un error."""
    if nombre in directorio_emails:
        return directorio_emails[nombre]
    else:
        # Lanzamos un error si no existe para que lo gestione el programa principal
        raise KeyError(f"El usuario '{nombre}' no existe en el diccionario.")