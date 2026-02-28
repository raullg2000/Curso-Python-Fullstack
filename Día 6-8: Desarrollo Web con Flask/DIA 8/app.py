from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# Funció per connectar a la BD (XAMPP)
def get_db_connection():
    return mysql.connector.connect(
        host="172.27.192.1", # La teva IP de Windows
        user="root",
        password="",
        database="ejercicios_python"
    )

# --- EXERCICI 1.2: Formulari 100 anys ---
@app.route('/centanys', methods=['GET', 'POST'])
def cent_anys():
    if request.method == 'POST':
        nom = request.form['nom']
        edat = int(request.form['edat'])
        any_100 = datetime.now().year + (100 - edat)
        return f"<h1>Hola {nom}, faràs 100 anys l'any {any_100}</h1>"
    return render_template('centanys_form.html')

# --- URL getmail: Busca i mostra mail ---
@app.route('/getmail', methods=['GET', 'POST'])
def get_mail():
    email_trobat = None
    error = None
    nom_buscat = None

    if request.method == 'POST':
        nom_buscat = request.form['nom']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT email FROM usuarios WHERE nombre = %s", (nom_buscat,))
        resultado = cursor.fetchone()
        conn.close()

        if resultado:
            email_trobat = resultado[0]
        else:
            error = f"L'usuari '{nom_buscat}' no existeix a la base de dades."

    return render_template('getmail.html', email=email_trobat, error=error, nom=nom_buscat)

# --- URL addmail: Afegeix nou usuari ---
@app.route('/addmail', methods=['GET', 'POST'])
def add_mail():
    missatge = None
    if request.method == 'POST':
        nom = request.form['nom']
        email = request.form['email']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO usuarios (nombre, email) VALUES (%s, %s)", (nom, email))
            conn.commit()
            missatge = f"Usuari {nom} afegit correctament!"
        except Exception as e:
            missatge = f"Error: {e}"
        finally:
            conn.close()

    return render_template('addmail.html', missatge=missatge)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)