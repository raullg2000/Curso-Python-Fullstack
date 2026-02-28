import mysql.connector

def get_mail():
    print("--- 🔍 Buscador de Emails (WSL -> Windows MySQL) ---")
    nombre_buscado = input("Introduce el nombre: ")

    try:
        # Usamos la IP de tu nameserver que salió en la terminal
        conexion = mysql.connector.connect(
            host="172.27.192.1", 
            user="root",
            password="",
            database="ejercicios_python"
        )
        
        cursor = conexion.cursor()
        query = "SELECT email FROM usuarios WHERE nombre = %s"
        cursor.execute(query, (nombre_buscado,))
        
        resultado = cursor.fetchone()
        
        if resultado:
            print(f"✅ Resultado: {resultado[0]}")
        else:
            print(f"⚠️ No se encontró a '{nombre_buscado}' en la base de datos.")

    except mysql.connector.Error as e:
        print(f"❌ Error de conexión: {e}")
        print("💡 Consejo: Asegúrate de que MySQL está en VERDE en XAMPP.")
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()

if __name__ == "__main__":
    get_mail()