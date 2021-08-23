import ast
import json, re
from flask import Flask, render_template, redirect, url_for, request
from airport_booking_system.airport_booking.flight_trip import FlightTrip
from airport_booking_system.airport_booking.plane import Plane
from config.definitions import json_path

app = Flask(__name__)


def read_file():
    with open(json_path + 'flight_trips.json', ) as flights:
        data = flights.read()
    return json.loads(data)


@app.route("/", methods=['POST', 'GET'])
def index():
    json_file = read_file()
    if request.method == 'GET':
        user = read_file()
        return render_template("index.html",
                               json_file=user)
    else:
        user = re.search("[^=][A-Z\d]+", str(request.get_data('fly'))).group()
        print(user, "000000", json_file[str(user)])
        # main=json_file[str(user)][0]

        return redirect(url_for('success', id=user))


@app.route('/create_flight', methods=["GET", "POST"])
def create_flight():
    with open(json_path + "planes.json", 'r') as jsonfile:
        planes = json.load(jsonfile)
    if request.method == 'POST':
        plane_dict = eval(request.form['planes'])
        print(plane_dict, type(plane_dict))
        plane_id = plane_dict['id']
        plane_cap = plane_dict['max_capacity']
        print(request.form['planes'])
        plane = Plane(plane_id, plane_cap)
        flight = FlightTrip(request.form['id'],
                            request.form['destination'],
                            request.form['time'],
                            request.form['duration'],
                            request.form['price'],
                            plane)
    return render_template('create_flight.html', plane_list=planes)


@app.route('/flight_trip/<id>', methods=['POST', 'GET'])
def success(id):
    if request.method == 'GET':
        user = read_file()
        return render_template("flight_trip.html",
                               plane_id=id,
                               data=user[id]
                               )


if __name__ == '__main__':
    app.debug = True
    app.run()
