#!/usr/bin/env python

from flask import Flask
from flask import render_template

from flask.ext.babel import Babel


app = Flask(__name__)
app.config.from_object('settings')
try:
    app.config.from_envvar('E110_SETTINGS')
except:
    pass

babel = Babel(app)


@app.route("/")
def hello():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
