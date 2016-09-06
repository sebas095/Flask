from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola Mundo <br><a href="/params">Link</a>'

@app.route('/params/')
@app.route('/params/<name>/')
@app.route('/params/<name>/<int:num>/')
def params(name = 'valor por default', num = 'nada'):
    return 'El parametro es: {} {}'.format(name, num)

if __name__ == '__main__':
    app.run(debug = True, port = 8000)
