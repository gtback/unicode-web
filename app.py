import unicodedata

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/<s>')
def hello(s=None):
    data = [(x, ord(x), unicodedata.name(x)) for x in s]
    return render_template('index.html', data=data, string=s)


if __name__ == "__main__":
    app.run()
