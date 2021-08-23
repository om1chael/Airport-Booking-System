from flask import Flask, render_template, redirect, url_for, request
import re
from Setup_Config.definitions import ROOT_DIR, json_path
import os
import json

app = Flask(__name__)
filepath = os.path.join(os.path.dirname(__file__))

dir="C:/Users/Sacha/GitRepos/Airport-Booking-System/airport_booking_system/airport_booking/"


def read_file():
    with open(dir +"flight_trips.json", ) as flights:
        data = flights.read()
    return json.loads(data)


@app.route("/", methods=['POST', 'GET'])
def index():
    json_file = read_file()
    print("2", type(json_file))
    if request.method == 'GET':
        user = json_file
        print(3, user)
        return render_template("index.html",
                               json_file=user)
    else:
        print("4",str(request.get_data('fly')))
        user = re.search("[^=][A-Z\d]+", str(request.get_data('fly'))).group()
        print(user, "000000", json_file[str(user)])

        return redirect(url_for('success', id=user))

@app.route('/create_flight', methods=["GET", "POST"])
def create_flight():
    flight_list = ['flight1', 'flight2']
    with open(json_path + "planes.json", 'r') as jsonfile:
        planes = json.load(jsonfile)
    if request.method == 'POST':
        create_json_flights_file('XY0123',
                                 request.form['destination'],
                                 request.form['time'],
                                 request.form['duration'],
                                 request.form['price'],
                                 'plane_id',
                                 "temporary_plane_cap")
    return render_template('create_flight.html', plane_list=planes)



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
