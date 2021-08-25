import json
from config.definitions import json_path


def create_json_flights_file(flight_id, destination, datetime, duration, price, plane_id, plane_maxcap):
    dict = {flight_id: [{
        "Destination": destination,
        "Date:Time": datetime,
        "Duration": duration,
        "Price": price,
        "Plane_ID": plane_id,
        "Plane_MaxCap": plane_maxcap
    }]}
    print(dict)

    with open(json_path + "flight_trips.json", "r+") as file:
        data = json.load(file)
        data.update(dict)
        file.seek(0)
        json.dump(data, file)
    return