from flask import Flask, render_template, request, jsonify
from othello import *
import othello

app = Flask(__name__)#nuevo objeto

#ruta inicial
@app.route('/')#wrap o un decorador
def index():
    title = 'Othello Angelo'
    score = 'Score'
    return render_template('index.html', title= title, score = score)

#ruta para endpoint: recibe cordenadas y devuelve la matriz actualizada
@app.route('/getPosition', methods=['POST'])
def getPosition():
    #paramentros que recibe: row, col, player
    row = request.json['row']
    col = request.json['col']
    player = request.json['player']
    #metodo de python que devuelve un string
    sms = othello.selectCell(row, col, player)
    return jsonify( grid=othello.grid, mensaje= sms)

#ruta para endpoint: no recibe nada solo devuelve la matriz
@app.route('/start', methods=['POST'])
def start():
    return jsonify( grid=othello.grid)

#ruta para endpoint: recibe una matriz de respaldo y la setea en python
@app.route('/reset', methods=['POST'])
def reset():
    othello.grid = request.json['respaldo']
    return jsonify( grid=othello.grid)

#onfiguraciones del servidor
if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, use_reloader=True)