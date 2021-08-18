from booking import Passenger

p = Passenger("Peter Random", "XY12345")

def test_passenger_name():
    assert p.give_name() == "Peter Random"

def test_passenger_passport():
    assert p.give_passport() == "XY12345"


def test_generate_report():
    pass

def test_plane_data():
    pass

def test_check_capacity():
    pass

def test_change_plane():
    pass

