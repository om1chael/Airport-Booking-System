from passengers import Passenger
from airport_planes import Plane

class Flight_Trip:
    def __init__(self, destination, datetime, duration, price, plane):
        self.destination = destination
        self.datetime = datetime
        self.duration = duration
        self.price = price
        self.people = []
        self.plane_id = plane.id
        self.plane_max = plane.max_capacity

       # self.current_capacity = plane.max_capacity-len(self.people)

    def set_plane(self, new_plane):
        if new_plane.max_capacity > len(self.people):
            self.plane_id = new_plane.id
            self.plane_max = new_plane.max_capacity
        else: print("Plane capacity is too small, you cannot choose this plane.")

    def return_capacity(self):
        return self.plane_max - len(self.people)

    def add_passenger(self, Passenger):
        if self.return_capacity() >= 1:
            self.people.append(Passenger.data)
        else: print("Plane is full")

    def generate_report(self):
        return self.people


p = Passenger("p","42")
#add.passenger(p)
pl = Plane("679", 10)
ft = Flight_Trip("paris", "dt", "2 hrs", "£5", pl)
ft.add_passenger(p)
ft.generate_report()
#print(ft.current_capacity)
print(ft.generate_report())
pl2 = Plane("t53", 15)

ft.set_plane(pl2)
print(ft.plane_id,ft.plane_max)
print(ft.people)
print(ft.return_capacity())



    # def give_destination(self):
    #     return self.destination
    #
    # def give_datetime(self):
    #     return datetime
    #
    # def give_duration(self):
    #     return self.duration
     def check_capacity():

