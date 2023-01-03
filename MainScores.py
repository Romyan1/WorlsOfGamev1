from flask import Flask, render_template
from pathlib import Path


app = Flask(__name__)
@app.route('/')
def score_server():
    try:
        scores_file = open(Path('Score.txt'), 'r')
        score = scores_file.read()
        return render_template('score.html', SCORE=score)
    except FileNotFoundError:
        return 'Not Found'


if __name__ == '__main__':
    app.run()
