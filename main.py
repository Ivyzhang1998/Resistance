"""
Author: Jiawen Zhang
Date: 10/18/2020
"""

from Game import Game
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    g = Game()
    g.assign_cards()
    g.do_all_missions()
    return render_template('index.html', logs = g.rounds_logs)
if __name__ == '__main__':
    app.run(debug=True)
