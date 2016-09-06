from flask import Flask

# Creamos la instancia
app = Flask(__name__)

@app.route('/') # wrap o decorador
def index():
    return 'Hola Mundo' # Regresa un string

app.run() # corre el servidor puerto default: 5000
