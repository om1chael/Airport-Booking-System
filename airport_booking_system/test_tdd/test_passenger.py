from airport_booking_system.airport_booking.passenger import Passenger
from airport_booking_system.airport_booking.plane import Plane
from airport_booking_system.airport_booking.flight_trip import FlightTrip

p = Passenger("Peter Random", "XY12345")
plane = Plane("QW12345", 100)
plane2 = Plane("AS12345", 50)
plane_full = Plane("AS12345", 0)
flight = FlightTrip("Madrid", "16:00 01/09/21", "3 hours", "£200.00", plane)
flight_full = FlightTrip("Madrid", "16:00 01/09/21", "3 hours", "£200.00", plane_full)


def test_passenger_name():
    assert p.give_name() == "Peter Random"


def test_passenger_passport():
    assert p.give_passport() == "XY12345"


def test_generate_report():
    flight.add_passenger(p)
    assert flight.generate_report() == [{'name': 'Peter Random', 'passport': 'XY12345'}]


def test_plane_data():
    assert plane.id == "QW12345"
    assert plane.max_capacity == 100


def test_flight_data():
    assert flight.destination == "Madrid"
    assert flight.datetime == "16:00 01/09/21"
    assert flight.duration == "3 hours"
    assert flight.plane_id == "QW12345"
    assert flight.plane_max == 100


def test_check_full_capacity():
    for i in range(flight.plane_max):
        flight.add_passenger(p)
    assert flight.return_capacity() == 0
    flight.add_passenger(p)
    assert flight.return_capacity() == 0
    assert flight.add_passenger(p) == "Plane is full"


def test_change_plane():
    for i in range(60):
        flight.add_passenger(p)
    assert flight.set_plane(plane2) == "Plane capacity is too small, you cannot choose this plane."
    flight.set_plane(plane2)
    assert flight.plane_id == "QW12345"  # Plane did not change
