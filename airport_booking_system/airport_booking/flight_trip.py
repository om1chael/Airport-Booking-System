import json
from config.definitions import json_path

class FlightTrip:
    def __init__(self, flight_id, destination, datetime, duration, price, plane):
        self.flight_id = flight_id.upper()
        self.destination = destination
        self.datetime = datetime
        self.duration = duration
        self.price = price
        self.people = []
        self.plane_id = plane.id
        self.plane_max = plane.max_capacity
        self.create_flight_trip()

    def create_flight_trip(self):
        flight_dict = {self.flight_id: [{
            "Destination": self.destination,
            "Date:Time": self.datetime,
            "Duration": self.duration,
            "Price": self.price,
            "Plane ID": self.plane_id,
            "Plane Maximum Capacity": self.plane_max
        }]}
        with open(json_path + "flight_trips.json", "r+") as file:
            data = json.load(file)
            data.update(flight_dict)
            file.seek(0)
            json.dump(data, file)

    def set_plane(self, new_plane):
        if new_plane.max_capacity > len(self.people):
            self.plane_id = new_plane.id
            self.plane_max = new_plane.max_capacity
        else:
            print("Plane capacity is too small, you cannot choose this plane.")
            return "Plane capacity is too small, you cannot choose this plane."

    def return_capacity(self):
        return self.plane_max - len(self.people)

    def add_passenger(self, passenger):
        if self.return_capacity() >= 1:
            self.people.append(passenger.data)
            with open(json_path + "passengers.json", "r+") as file:
                data = json.load(file)
                data.update(dict)
                file.seek(0)
                json.dump(data, file)
            return
        else:
            print("Plane is full")
            return "Plane is full"

    def generate_report(self):
        return self.people



# p = Plane("QW123", 100)
# f = FlightTrip("ASDFF123", "destination", "datetime", "duration", 4, p)
# pas = Passenger("Peter", "BV6543")
# f.add_passenger(pas)
#
# print(f.people)