import json
from config.definitions import json_path
from airport_booking_system.airport_booking.plane import Plane

# Define Flight Trip class
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
            "Date-Time": self.datetime,
            "Duration": self.duration,
            "Price": self.price,
            "Plane_ID": self.plane_id,
            "Plane Maximum Capacity": self.plane_max
        }]}
        with open(json_path + "flight_trips.json", "r+") as file:
            data = json.load(file)
            data.update(flight_dict)
            file.seek(0)
            json.dump(data, file)

    # Assigns a new plane if the max capacity of the new plane is greater than the number of passengers on the flight
    def set_plane(self, flight_id, new_plane):
        # self.plane_id = new_plane.id
        # self.plane_max = new_plane.max_capacity
        with open(json_path + "flight_trips.json", "r+") as file:
            data = json.load(file)
            data[flight_id][0]["Plane_ID"] = new_plane
            file.seek(0)
            json.dump(data, file)

    # Returns the available capacity on the plane
    def return_capacity(self):
        return self.plane_max - len(self.people)

    # Adds a passenger to the flight if the flight capacity is greater than zero
    def add_passenger(self, passenger):
        if self.return_capacity() > 0:
            self.people.append(passenger.data)
            with open(json_path + "passengers.json", "r+") as file:
                data = json.load(file)
                data.update(dict)
                file.seek(0)
                json.dump(data, file)
            return
        else:
            return "Plane is full"

    # Generates report of the list of passengers on the flight
    def generate_report(self):
        return self.people
