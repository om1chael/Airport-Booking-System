import json
from definitions import ROOT_DIR, json_path
from airport_booking_system.airport_booking.flight_trip import FlightTrip
from airport_booking_system.airport_booking.plane import Plane
from airport_booking_system.airport_booking.json_planes import create_json_planes_file



def create_json_flights_file(destination, datetime, duration, price, plane_id, plane_maxcap):
    flights_dict = {
        "Destination": destination,
        "Date:Time": datetime,
        "Duration": duration,
        "Price": price,
        "Plane ID": plane_id,
        "Plane Maximum Capacity": plane_maxcap
    }
    with open(json_path + "flight_trips.json", "r") as file:
        if file:
            data = json.load(file)
            data.append(flights_dict)
    with open(json_path + "flight_trips.json", "w") as file:
        json.dump(data, file)
    return
