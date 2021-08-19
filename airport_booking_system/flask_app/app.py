from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data', methods=["GET", "POST"])
def data():
    if request.method == "GET":
        return '<h1>Data works</h1>'
    elif request.method == "POST":
        return 'POST'


if __name__ == '__main__':
    app.debug = True
    app.run()
