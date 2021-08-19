import json
from plane import Plane


def create_json_planes_file(plane_id, plane_cap):
    dict = {
        "id": plane_id,
        "max capacity": plane_cap
            }
    with open("planes.json", "r") as file:
        data = json.load(file)
    data.append(dict)
    with open("planes.json", "w") as file:
        json.dump(data, file)
    return



