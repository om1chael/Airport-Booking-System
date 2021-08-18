from airport_booking_system.airport_booking.booking import Passenger
# from airport_booking_system.airport_booking.booking import Plane
import unittest
import pytest

p = Passenger("Peter Random", "XY12345")
plane = Plane("QW12345", 100)
plane_full = Plane("AS12345", 0)
flight = FlightTrip("Madrid", "16:00 01/09/21", "3 hours", plane, "£200.00")
flight_full = FlightTrip("Madrid", "16:00 01/09/21", "3 hours", plane_full, "£200.00")


def test_passenger_name():
    assert p.give_name() == "Peter Random"


def test_passenger_passport():
    assert p.give_passport() == "XY12345"


def test_generate_report():
    pass


def test_plane_data():
    assert plane.id == "QW12345"
    assert plane.max_capacity == 100

def test_flight_data():
    assert flight.destination == "Madrid"
    assert flight.time_date == "16:00 01/09/21"
    assert flight.duration == "3 hours"
    assert flight.plane.id == "QW12345"
    assert flight.plane.max_capacity == 100

def test_flight_sell_ticket():
    assert p in flight.people == True


def test_check_capacity():
    assert flight.is_capacity() == True
    assert flight_full.is_capacity() == False


def test_change_plane():
    pass
