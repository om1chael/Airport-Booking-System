# Defines Passenger class
import json
import os

from Project.Setup_and_Configurations.definitions import ROOT_DIR
class Passenger:
    def __init__(self,plane_id ,passport, name):
        self.name = name
        self.passport = passport
        self.plane_id = plane_id
        self.templte = {self.plane_id :[{self.passport:self.name}]}
        self.create_default_file()



    # Returns name of passenger
    def give_name(self):
        return self.name

    # Returns passport number of passenger
    def give_passport(self):
        return self.passport

    def create_default_file(self):
        with open("passengers.json", "r+") as file:
            data = json.load(file)
            if(self.plane_id not in data.keys()):
                file.seek(0)
                data[self.plane_id]=[{"-":"-"}]
                json.dump(data, file)


    def create_json_passenger_file(self):
        ## The jason file has a a plane ID.
        ## Each plane ID has a user
        ##
        #if(self.New_passnger_check()):
        with open("passengers.json", "r+") as file:
            data = json.load(file)
            if self.plane_id in data.keys():
                data[self.plane_id][0][self.passport]=self.name
            else:
                data.update(self.templte)
            file.seek(0)
            print("DONEE")
            print("DONE",data)
            json.dump(data,file)
#            file.close()
        #else:
         #   return "Passport ID already exists"

    def New_passnger_check(self):
         with open("passengers.json", "r+") as file:
             passenger_list = json.load(file)

         for flights in passenger_list.keys():
             pass_data = passenger_list[flights][0]
             if self.passport in pass_data.keys():
                 return False
             else:
                return True







#f = Passenger("AI-RE","NZLD","Sam")
#f.create_json_passenger_file()
#print(f.New_passnger_check())
#with open("passengers.json", "r") as file_:
 #   print(json.load(file_))
