from .models import BoardingPass
from .exceptions import OverWeightLuggageError, FlightFullError

class CheckInCounter():
    def __init__(self, counter_id, flight, queue):
        self.counter_id = counter_id
        self.flight = flight
        self.queue = queue

    def check_in(self, passenger, luggage_list):
        if self.flight.is_full():
            raise FlightFullError("The flight is full. Cannot check in.")
        
        seat = self.flight.assign_seat()

        for luggage in luggage_list:
            luggage.validate_weight()

        boarding_pass = BoardingPass(passenger, self.flight, seat, luggage_list)

        self.flight.add_boarding_pass(boarding_pass)

        return boarding_pass
            
    def process_queue(self, luggage_by_booking):
        while not self.queue.is_empty():
            passenger = self.queue.next_passenger()
            luggage_list = luggage_by_booking.get(passenger.booking_ref, [])
            try:
                result = self.check_in(passenger, luggage_list)
            except (FlightFullError, OverWeightLuggageError) as error:
                result = error 

            yield result
        