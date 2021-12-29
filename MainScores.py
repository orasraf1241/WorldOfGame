from flask import Flask, render_template
from flask import request
from Utils import SCORES_FILE_NAME

app = Flask(__name__)


@app.route('/')
def score_server():
    try:
        file = open(SCORES_FILE_NAME, 'r+')
        test = file.read()
        file.close()
        return render_template("Score.html", SCORE=test)
    except OSError:
        error = "OSerror"
        return render_template("Error.html", ERROR=error)
