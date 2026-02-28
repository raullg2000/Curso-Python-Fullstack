from flask import Flask, render_template # Cambiamos esto
from datetime import datetime

app = Flask(__name__)

@app.route('/parellsenar/<int:numero>')
def parell_senar(numero):
    res = "PARELL" if numero % 2 == 0 else "SENAR"
    return f"El número {numero} és {res}"

@app.route('/centanys/<nom>/<int:edat>')
def cent_anys(nom, edat):
    any_100 = datetime.now().year + (100 - edat)
    # Ahora enviamos los datos al archivo HTML externo
    return render_template('resultado.html', nombre=nom, edat=edat, any_100=any_100)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)