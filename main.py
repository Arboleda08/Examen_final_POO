from airport.models import Passenger, Flight, CarryOn, CheckedLuggage, BoardingPass
from airport.queueing import CheckInQueue
from airport.counter import CheckInCounter
from airport.exceptions import EmptyQueueError

def main():
    vuelo = Flight("V001","Bogota", "2026-06-10 08:30", 2)

    Passanger1 = Passenger("Ana Torres", "1020304050", "BR001", False)
    Passanger2 = Passenger("Luis Perez", "9988776655", "BR002", True)
    Passanger3 = Passenger("Marta Ruiz", "1122334455", "BR003", False)
    Luggage1 = CarryOn(8.5, "TAG001")
    Luggage2 = CheckedLuggage(20.0, "TAG002")
    pass1 = BoardingPass(Passanger1, vuelo, "A1", [Luggage1])
    pass2 = BoardingPass(Passanger2, vuelo, "A2", [Luggage2])
    baggage_per_reservation = {
        "BR001": [CarryOn(8.5, "TAG001"), CheckedLuggage(20.0, "TAG002")],
        "BR002": [CheckedLuggage(30.0, "TAG003")],   # sobrepeso -> rechazo
        "BR003": [CarryOn(5.0, "TAG004")],
    }

    queue = CheckInQueue()
    registercounter = CheckInCounter("C1", vuelo, queue)
 
    queue.enqueue(Passanger1)
    queue.enqueue(Passanger2)
    queue.enqueue(Passanger3)

    print("Procesing the check-in queue")
    for result in registercounter.process_queue(baggage_per_reservation):
        if isinstance(result, BoardingPass):
            print(result.print_pass())
        else:
            print(f"Error: {result}")

    print("\nFinal Boarding Passes:")
    for boarding_pass in vuelo:
        print(boarding_pass.print_pass())

    print("\n next passenger in the queue:")
    try:
        next_passenger = queue.next_passenger()
        print(f"Next passenger: {next_passenger.get_name()} (ID: {next_passenger.get_masked_id()})")
    except EmptyQueueError as e:
        print(f"Error: {e}")
        
if __name__ == "__main__":
    main()