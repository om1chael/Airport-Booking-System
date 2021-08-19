import json
from flight_trip import FlightTrip
from plane import Plane
from json_planes import create_json_planes_file


def create_json_flights_file(destination, datetime, duration, price, plane_id, plane_maxcap):
    dict = {
        "Destination":destination,
        "Date:Time": datetime,
        "Duration":duration,
        "Price": price,
        "Plane ID": plane_id,
        "Plane Maximum Capacity": plane_maxcap
    }
    with open("flight_trips.json", "r") as file:
        data = json.load(file)
    data.append(dict)
    with open("flight_trips.json", "w") as file:
        json.dump(data, file)
    return


plane = Plane("FD234", 80)
create_json_planes_file(plane.id, plane.max_capacity)
ft = FlightTrip("France", "14/9 13:00", 2, "200", plane)
create_json_flights_file(ft.destination, ft.datetime, ft.duration, ft.price, ft.plane_id, ft.plane_max)