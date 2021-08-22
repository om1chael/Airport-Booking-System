import flask
from flask import Flask, render_template, redirect, url_for, request
import requests
import re
import os
from definitions import ROOT_DIR, json_path
import json

app = Flask(__name__)
filepath = os.path.join(os.path.dirname(__file__) + "/current_flights.json")


# current_flights.json
def read_file():
    with open(json_path + 'flight_trips.json', ) as flights:
        data = flights.read()
        print(type(data))
    return json.loads(data)

@app.route("/", methods=['POST', 'GET'])
def index():
    json_file = read_file()
    print("2", type(json_file))
    if request.method == 'GET':
        user = read_file()
        print(3, user)
        return render_template("index.html",
                               json_file=user)
    else:
        user = re.search("[^=][A-Z\d]+", str(request.get_data('fly'))).group()
        print(user, "000000", json_file[str(user)])

        main = json_file[str(user)][0]
        locat = main["Destination"]
        time = main["Time"]

        # main=json_file[str(user)][0]

        return redirect(url_for('success', id=user))


@app.route('/success/<id>', methods=['POST', 'GET'])
def success(id):
    if request.method == 'GET':
        user = read_file()
        return render_template("third_page.html",
                               plane_id=id,
                               data=user[id]
                               )


# response_code = requests.get("http://127.0.0.1:5000/")
# print(response_code)

@app.route("/api", methods=["GET", "POST"])
def data():
    if request.method == "GET":
        return '<h1 style ="post:green"> The test works </h1>'
    elif request.method == "POST":
        return 'POST'


if __name__ == "__main__":
    app.debug = True
    app.run()
