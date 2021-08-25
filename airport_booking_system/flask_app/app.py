import json
import re
from flask import Flask, flash, render_template, redirect, url_for, request
from airport_booking_system.airport_booking import passenger
from airport_booking_system.airport_booking.flight_trip import FlightTrip
from airport_booking_system.airport_booking.plane import Plane
from config.definitions import json_path

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

with open(json_path + "planes.json", 'r') as jsonfile:
    planes = json.load(jsonfile)


def read_file(file_name):
    with open(json_path + file_name) as flights:
        data = flights.read()
    return json.loads(data)


def set_plane(old_flight_id, plane_id, plane_max):
    # load JSON file and convert it to dict
    file = dict(read_file("flight_trips.json"))
    # change the json file by assigning the new values
    file[old_flight_id][0]["Plane_ID"] = plane_id
    file[old_flight_id][0]["Plane Maximum Capacity"] = plane_max
    # dump that alternated dict into the json file
    with open(json_path + "flight_trips.json", "w") as f:
        json.dump(file, f, ensure_ascii=False, indent=4)


def create_default_file(plane_id):
    with open(json_path + "passengers.json", "r+") as file:
        data = json.load(file)
        if plane_id not in data.keys():
            file.seek(0)
            data[plane_id.upper()] = [{}]
            print("Create_Data", data)
            json.dump(data, file)


@app.route("/", methods=['POST', 'GET'])
def index():
    json_file = read_file("flight_trips.json")
    if request.method == 'GET':
        user = read_file('flight_trips.json')
        return render_template("index.html",
                               json_file=user)
    else:
        user = re.search("[^=][A-Z\d]+", str(request.get_data('fly'))).group()
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
        create_default_file(request.form['id'])
        flash('Flight created')
    return render_template('create_flight.html', plane_list=planes)


@app.route('/flight_trip/<id>', methods=['POST', 'GET'])
def flight_trip(id):
    pass_file = read_file('passengers.json')
    user = read_file('flight_trips.json')
    if request.method == 'GET':
        return render_template("flight_trip.html",
                               Flight_id=id,
                               data=user[id],
                               pass_info=pass_file[id][0],
                               # data=read_file()[id],
                               plane_id=id,
                               plane_list=planes
                               )

    if request.method == "POST":
        if request.form.get("planes") is not None:
            plane_dict = eval(request.form['planes'])
            print("if statement dict", plane_dict)
            plane_id = plane_dict['id']
            plane_cap = plane_dict['max_capacity']
            set_plane(id, plane_id, plane_cap)
        else:
            pass_id = request.form["passport_ID"]
            name = request.form["Name"]
            creat_pass = passenger.Passenger(id, pass_id, name)
            creat_pass.create_json_passenger_file()
            flash('Passenger added')
        passenger_count = len(pass_file[id][0])
        space_left = user[id][0]["Plane Maximum Capacity"] - passenger_count
        return render_template("flight_trip.html",
                               flight_id=id,
                               plane_list=planes,
                               data=user[id],
                               pass_info=pass_file[id][0],
                               Seats_left=space_left
                               )

if __name__ == '__main__':
    app.debug = True
    app.run()
