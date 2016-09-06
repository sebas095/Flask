from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola Mundo <br><a href="/saluda">Link</a>'

@app.route('/saluda')
def saluda():
    return 'Otro mensaje <br><a href="/">Volver</a>'

@app.route('/params')
def params():
    # ?params=valor
    param1 = request.args.get('params1', 'no contiene este parametro')
    param2 = request.args.get('params2', 'no contiene este parametro')
    return 'Los parametros son {}, {}'.format(param1, param2)

if __name__ == '__main__':
    app.run(debug = True, port = 8000)
