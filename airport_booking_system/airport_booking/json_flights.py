import json
from definitions import ROOT_DIR, json_path
from airport_booking_system.airport_booking.flight_trip import FlightTrip
from airport_booking_system.airport_booking.plane import Plane
from airport_booking_system.airport_booking.json_planes import create_json_planes_file


# import Class that will be used by Flask and in JSON file

def create_json_flights_file(destination, datetime, duration, price, plane_id, plane_maxcap):
    # create a new key (flight ID) with a list of the flight details as the value
    # add to the dictionary in the JSON file
    # values come from FlightTrip class
    flights_dict = {
        "Destination": destination,


def create_json_flights_file(flight_id, destination, datetime, duration, price, plane_id, plane_maxcap):
    dict = {flight_id: [{
        "Destination":destination,
        "Date:Time": datetime,
        "Duration": duration,
        "Price": price,
        "Plane ID": plane_id,
        "Plane Maximum Capacity": plane_maxcap
    }
<<<<<<< HEAD

    with open(json_path + "flight_trips.json", "r") as file:
        if file:
            data = json.load(file)
            data.append(flights_dict)
    with open(json_path + "flight_trips.json", "w") as file:
=======
      


    with open(json_path + "flight_trips.json", "r+") as file:
        data = json.load(file)
        data.update(dict)
        file.seek(0)
>>>>>>> 9135eff6df0c861fbfee73de9eddb00ec8f182aa
        json.dump(data, file)
    return


plane = Plane("FD234", 80)
create_json_planes_file(plane.id, plane.max_capacity)
ft = FlightTrip("AS987", "France", "14/9 13:00", 2, "200", plane)
#
create_json_flights_file(ft.flight_id, ft.destination, ft.datetime, ft.duration, ft.price, ft.plane_id, ft.plane_max)

