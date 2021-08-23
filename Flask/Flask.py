import flask
from flask import Flask, render_template, redirect, url_for, request
import requests
import re
import os
from Project.Setup_and_Configurations.definitions import ROOT_DIR, json_path
import json
from Project.airport_booking_system.airport_booking import passenger
import pathlib
app = Flask(__name__)

# current_flights.json
def read_file(file_name):
    with open( file_name, ) as flights:
        data = flights.read()
    return json.loads(data)



@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'GET':

        user = read_file("flight_trips.json")
        return render_template("index.html",
                               json_file=user)
    else:
        user = re.search("[^=][A-Z\d]+", str(request.get_data('fly'))).group()
       # print(user, "000000", json_file[str(user)])

        return redirect(url_for('success', id=user))


@app.route('/success/<id>', methods=['POST', 'GET'])
def success(id):
    pass_file = read_file('passengers.json')
    user = read_file('flight_trips.json')

    if request.method == 'GET':
        return render_template("third_page.html",
                               plane_id=id,
                               data=user[id],
                               pass_info=pass_file[id][0])
    else:

        pass_id = request.form["passport_ID"]
        name = request.form["Name"]
        creat_pass=passenger.Passenger(id,pass_id ,name)
        creat_pass.create_json_passenger_file()
        return render_template("third_page.html",
                               plane_id=id,
                               data=user[id],
                               pass_info=pass_file[id][0]

                               )




if __name__ == "__main__":
    app.debug = True
    app.run()
