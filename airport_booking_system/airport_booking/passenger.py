
class Passenger:
    def __init__(self, name, passport):
        self.name = name
        self.passport = passport
        self.data = {
            "name": name,
            "passport": passport
        }

    def give_name(self):
        return self.name

    def give_passport(self):
        return self.passport

    def give_details(self):
        return self.data