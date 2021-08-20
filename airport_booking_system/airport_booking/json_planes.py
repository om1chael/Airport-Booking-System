import json
from definitions import ROOT_DIR, json_path
from airport_booking_system.airport_booking.plane import Plane


def create_json_planes_file(plane_id, plane_cap):
    planes_dict = {
        "id": plane_id,
        "max capacity": plane_cap
            }
    with open(json_path + "planes.json", "r") as file:
        data = json.load(file)
    data.append(planes_dict)
    with open(json_path + "planes.json", "w") as file:
        json.dump(data, file)
    return

