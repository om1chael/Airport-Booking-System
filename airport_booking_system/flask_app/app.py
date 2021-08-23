import ast
import json, re
from flask import Flask, render_template, redirect, url_for, request
from airport_booking_system.airport_booking.flight_trip import FlightTrip
from airport_booking_system.airport_booking.plane import Plane
from config.definitions import json_path

app = Flask(__name__)

with open(json_path + "planes.json", 'r') as jsonfile:
    planes = json.load(jsonfile)


def read_file():
    with open(json_path + 'flight_trips.json', ) as flights:
        data = flights.read()
    return json.loads(data)


def set_plane(old_flight_id, plane_id, plane_max):
    # self.plane_id = new_plane.id
    # self.plane_max = new_plane.max_capacity
    with open(json_path + "flight_trips.json", "r+") as file:
        data = json.load(file)
        data[old_flight_id][0]["Plane_ID"] = plane_id
        data[old_flight_id][0]["Plane Maximum Capacity"] = plane_max
        file.seek(0)
        json.dump(data, file)


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

        return redirect(url_for('flight_trip', id=user))


@app.route('/create_flight', methods=["GET", "POST"])
def create_flight():
    if request.method == 'POST':
        plane_dict = eval(request.form['planes'])
        plane_id = plane_dict['id']
        plane_cap = plane_dict['max_capacity']
        plane = Plane(plane_id, plane_cap)
        flight = FlightTrip(request.form['id'],
                            request.form['destination'],
                            request.form['time'],
                            request.form['duration'],
                            request.form['price'],
                            plane)
    return render_template('create_flight.html', plane_list=planes)


@app.route('/flight_trip/<id>', methods=['POST', 'GET'])
def flight_trip(id):
    if request.method == 'GET':
        return render_template("flight_trip.html",
                               flight_id=id,
                               data=read_file()[id],
                               plane_list=planes
                               )
    if request.method == 'POST':
        plane_dict = eval(request.form['planes'])
        plane_id = plane_dict['id']
        plane_cap = plane_dict['max_capacity']
        set_plane(id, plane_id, plane_cap)
        return render_template("flight_trip.html",
                               flight_id=id,
                               data=read_file()[id],
                               plane_list=planes)


if __name__ == '__main__':
    app.debug = True
    app.run()
