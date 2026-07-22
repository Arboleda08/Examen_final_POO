from airport.models import Passenger, Flight, CarryOn, CheckedLuggage, BoardingPass
from airport.queueing import CheckInQueue
from airport.counter import CheckInCounter
from airport.exceptions import EmptyQueueError

def main():
    vuelo = Flight("V001","Bogota", "2026-06-10 08:30", 2)

    pasajero1 = Passenger("Ana Torres", "1020304050", "BR001", False)
    pasajero2 = Passenger("Luis Perez", "9988776655", "BR002", True)
    pasajero3 = Passenger("Marta Ruiz", "1122334455", "BR003", False)
    equipaje1 = CarryOn(8.5, "TAG001")
    equipaje2 = CheckedLuggage(20.0, "TAG002")
    pass1 = BoardingPass(pasajero1, vuelo, "A1", [equipaje1])
    pass2 = BoardingPass(pasajero2, vuelo, "A2", [equipaje2])
    pass1.print_pass()
    pass2.print_pass()

if __name__ == "__main__":
    main()