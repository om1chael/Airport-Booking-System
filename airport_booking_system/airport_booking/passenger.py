# Defines Passenger class

class Passenger:
    def __init__(self, plane_id, name, passport):
        self.name = name
        self.passport = passport
        self.plane_id = plane_id
        self.data = {self.plane_id: [{
            "name": name,
            "passport": passport
        }]}

    # Returns name of passenger
    def give_name(self):
        return self.name

    # Returns passport number of passenger
    def give_passport(self):
        return self.passport

    # Returns dictionary with name and passport number of each passenger
    def give_details(self):
        return self.data
