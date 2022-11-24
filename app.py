# SPDX-FileCopyrightText: 2022 Greg Back <git@gregback.net>
# SPDX-License-Identifier: MIT

import unicodedata

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/<s>')
def hello(s=None):
    if not s:
        return "Add a string to the URL"
    data = [(x, ord(x), unicodedata.name(x), unicodedata.category(x)) for x in s]
    return render_template('index.html', data=data, string=s)


if __name__ == "__main__":
    app.run()
