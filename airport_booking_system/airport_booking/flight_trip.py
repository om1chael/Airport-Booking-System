from airport_booking_system.airport_booking.passenger import Passenger
from airport_booking_system.airport_booking.plane import Plane


class FlightTrip:
    def __init__(self, destination, datetime, duration, price, plane):
        self.destination = destination
        self.datetime = datetime
        self.duration = duration
        self.price = price
        self.people = []
        self.plane_id = plane.id
        self.plane_max = plane.max_capacity

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
        else:
            print("Plane is full")
            return "Plane is full"

    def generate_report(self):
        return self.people

