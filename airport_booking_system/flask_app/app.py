import json
import re
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_wtf.csrf import CSRFProtect
from airport_booking_system.airport_booking import passenger
from airport_booking_system.airport_booking.flight_trip import FlightTrip
from airport_booking_system.airport_booking.plane import Plane
from config.definitions import json_path
from forms import CreateFlightForm, AddPassengerForm
import os


app = Flask(__name__)
csrf = CSRFProtect()

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
csrf.init_app(app)

with open(json_path + "planes.json", 'r') as jsonfile:
    planes = json.load(jsonfile)


def read_file(file_name):
    with open(json_path + file_name) as flights:
        data = flights.read()
    return json.loads(data)


def set_plane(old_flight_id, plane_id, plane_max):
    with open(json_path + "flight_trips.json", "r+") as file:
        data = json.load(file)
        data[old_flight_id][0]["Plane_ID"] = plane_id
        data[old_flight_id][0]["Plane Maximum Capacity"] = plane_max
        file.seek(0)
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
    form = CreateFlightForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            plane_dict = eval(request.form['planes'])
            plane_id = plane_dict['id']
            plane_cap = plane_dict['max_capacity']
            plane = Plane(plane_id, plane_cap)
            flight = FlightTrip(request.form['id'],
                                request.form['destination'],
                                request.form['time'],
                                request.form['duration'],
                                request.form['price'], plane)
        else:
            flash("Try again")
    return render_template('create_flight.html', plane_list=planes, form=form)

@app.route('/flight_trip/<id>', methods=['POST', 'GET'])
def flight_trip(id):
    pass_file = read_file('passengers.json')
    user = read_file('flight_trips.json')
    if request.method == 'GET':
        print('get')
        return render_template("flight_trip.html",
                               Flight_id=id,
                               data=user[id],
                               pass_info=pass_file[id][0],
                               # data=read_file()[id],
                               plane_id=id,
                               plane_list=planes
                               )
    else:
        print('post')
        pass_id = request.form["passport_ID"]
        name = request.form["Name"]
        creat_pass = passenger.Passenger(id, pass_id, name)
        creat_pass.create_json_passenger_file()
        return render_template("flight_trip.html",
                               flight_id=id,
                               plane_list=planes,
                               data=user[id],
                               pass_info=pass_file[id][0])


if __name__ == '__main__':
    app.debug = True
    app.run()
