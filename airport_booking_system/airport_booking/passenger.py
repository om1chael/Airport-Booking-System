class Passenger:
    def __init__(self, plane_id, name, passport):
        self.name = name
        self.passport = passport
        self.plane_id = plane_id
        self.data = {self.plane_id: [{
            "name": name,
            "passport": passport
        }]}

    def give_name(self):
        return self.name

    def give_passport(self):
        return self.passport

    def give_details(self):
        return self.data
