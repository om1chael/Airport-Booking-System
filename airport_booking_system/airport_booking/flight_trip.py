from airport_booking_system.airport_booking.passenger import Passenger
from airport_booking_system.airport_booking.plane import Plane


# Define Flight Trip class
class FlightTrip:
    def __init__(self, flight_id: str, destination, datetime, duration, price, plane):
        self.flight_id = flight_id.upper()
        self.destination = destination
        self.datetime = datetime
        self.duration = duration
        self.price = price
        self.people = []
        self.plane_id = plane.id
        self.plane_max = plane.max_capacity

    # Assigns a new plane if the max capacity of the new plane is greater than the number of passengers on the flight
    def set_plane(self, new_plane):
        if new_plane.max_capacity > len(self.people):
            self.plane_id = new_plane.id
            self.plane_max = new_plane.max_capacity
        else:
            return "Plane capacity is too small, you cannot choose this plane."

    # Returns the available capacity on the plane
    def return_capacity(self):
        return self.plane_max - len(self.people)

    # Adds a passenger to the flight if the flight capacity is greater than zero
    def add_passenger(self, passenger):
        if self.return_capacity() > 0:
            self.people.append(passenger.data)
        else:
            return "Plane is full"

    # Generates report of the list of passengers on the flight
    def generate_report(self):
        return self.people
