from .exceptions import OverWeightLuggageError
from abc import ABC, abstractmethod

class Passenger:
    def __init__(self, name, document_id, booking_ref, is_vip= False):
        self.name = name
        self.__document_id = document_id
        self.booking_ref = booking_ref
        self.is_vip = is_vip

    def get_masked_id(self):
        document = str(self.__document_id)
        return "*" * (len(document) - 4) + document[-4:]
    
    def get_name(self):
        return self.name
    

class Flight:
    def __init__(self, code, destination, departure, capacity = 0):
        self.code = code
        self.destination = destination
        self.departure = departure
        self.capacity = capacity
        self._assigned_seats = []
        self._boarding_passes = []

    def assign_seat(self):
        seat = len(self._assigned_seats) + 1
        self._assigned_seats.append(seat)
        return seat
    
    def available_seats(self):
        return self.capacity - len(self._assigned_seats)
    
    def is_full(self):
        return self.available_seats() <= 0
    
    def add_boarding_pass(self, boarding_pass):
        self._boarding_passes.append(boarding_pass)
    
    def __iter__(self):
        for boarding_pass in self._boarding_passes:
            yield boarding_pass


class Luggage(ABC):

    def __init__(self, weight, _tag_id):
        self.weight = weight
        self._tag_id =_tag_id

    @abstractmethod
    def validate_weight(self):
        pass

    def get_tag(self):
        return self._tag_id
    

class CarryOn(Luggage):
    def validate_weight(self):
        if self.weight > 10:
            raise OverWeightLuggageError(f"Carry-on luggage exceeds the weight limit of 10 kg. Current weight: {self.weight} kg.")
        else: 
            return True
        

class CheckedLuggage(Luggage):
    def validate_weight(self):
        if self.weight > 23:
            raise OverWeightLuggageError(f"Checked luggage exceeds the weight limit of 23 kg. Current weight: {self.weight} kg.")
        else:
            return True

class BoardingPass:
    def __init__(self, passenger, flight, seat, luggage_list):
        self.passenger = passenger
        self.flight = flight
        self.seat_number = seat
        self.luggage_list = luggage_list

    def print_pass(self):
        tags = [luggage.get_tag() for luggage in self.luggage_list]

        return (f"Boarding Pass for {self.passenger.get_name()} (ID: {self.passenger.get_masked_id()})\n"
                f"Flight: {self.flight.code} to {self.flight.destination}\n"
                f"Departure: {self.flight.departure}\n"
                f"Seat Number: {self.seat_number}\n"
                f"Luggage Tags: {', '.join(tags)}")