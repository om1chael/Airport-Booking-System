import json
from flask import Flask, render_template, request, jsonify
from airport_booking_system.airport_booking.json_flights import create_json_flights_file
from definitions import ROOT_DIR, json_path

app = Flask(__name__)


@app.route('/')
def index():
    flight_list = ['flight1', 'flight2']
    if request.method == 'POST':
        FlightList = request.form['dropdown']
    return render_template('index.html', flight_list=flight_list)


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


@app.route('/flight_trip')
def flight_trip():
    return render_template('flight_trip.html')


# @app.route('/data', methods=["GET", "POST"])
# def data():
#     if request.method == "GET":
#         return '<h1>Data works</h1>'
#     elif request.method == "POST":
#         return 'POST'


if __name__ == '__main__':
    app.debug = True
    app.run()
