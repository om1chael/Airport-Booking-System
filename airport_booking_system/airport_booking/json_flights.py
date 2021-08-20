import json
from definitions import ROOT_DIR, json_path
from airport_booking_system.airport_booking.flight_trip import FlightTrip
from airport_booking_system.airport_booking.plane import Plane
from airport_booking_system.airport_booking.json_planes import create_json_planes_file



def create_json_flights_file(destination, datetime, duration, price, plane_id, plane_maxcap):
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
      


    with open(json_path + "flight_trips.json", "r+") as file:
        data = json.load(file)
        data.update(dict)
        file.seek(0)
        json.dump(data, file)
    return


plane = Plane("FD234", 80)
create_json_planes_file(plane.id, plane.max_capacity)
ft = FlightTrip("AS987", "France", "14/9 13:00", 2, "200", plane)
#
create_json_flights_file(ft.flight_id, ft.destination, ft.datetime, ft.duration, ft.price, ft.plane_id, ft.plane_max)

