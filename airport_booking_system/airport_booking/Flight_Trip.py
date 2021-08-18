from passengers import Passenger
import Plane

class Flight_Trip:
    def __init__(self, destination, datetime, duration, price, plane):
        self.destination = destination
        self.datetime = datetime
        self.duration = duration
        self.price = price
        self.people = []

    def add_passenger(self, Passenger):
        self.people.append(Passenger.data)




    # def give_destination(self):
    #     return self.destination
    #
    # def give_datetime(self):
    #     return datetime
    #
    # def give_duration(self):
    #     return self.duration
     def check_capacity():

