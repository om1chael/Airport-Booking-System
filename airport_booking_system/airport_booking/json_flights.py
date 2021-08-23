import json
from Project.config.definitions import json_path


# Import Class that will be used by Flask and in JSON file

def create_json_flights_file(flight_id, destination, datetime, duration, price, plane_id, plane_maxcap):
    # Create a new key (flight ID) with a list of the flight details as the value
    # Add to the dictionary in the JSON file
    # Values come from FlightTrip class
    dict = {flight_id: [{
        "Destination": destination,
        "Date:Time": datetime,
        "Duration": duration,
        "Price": price,
        "Plane_ID": plane_id,
        "Plane Maximum Capacity": plane_maxcap
    }

    with open(json_path + "flight_trips.json", "r") as file:
        if file :
            data = json.load(file)
            data.append(flights_dict)
    with open(json_path + "flight_trips.json", "w") as file:



    }]}

    with open(json_path + "flight_trips.json", "r+") as file:
        data = json.load(file)
        data.update(dict)
        file.seek(0)

        json.dump(data, file)
    return


 plane = Plane("FD234", 80)
 create_json_planes_file(plane.id, plane.max_capacity)
 ft = FlightTrip("AS987", "Germany", "14/9 13:00", 10, "200", plane)
 #
 create_json_flights_file(ft.flight_id, ft.destination, ft.datetime, ft.duration, ft.price, ft.plane_id, ft.plane_max)
