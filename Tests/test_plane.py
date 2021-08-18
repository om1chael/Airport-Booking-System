## Tests ##
import pytest
import unittest

from Passengers import Passenger

Pass = Passenger("john", "AB23O023")

def Test_PassengerName():
    assert Pass.give_name() == "john"

def Test_PassengerPassport():
    assert Pass.give_passport() == "AB23O023"
