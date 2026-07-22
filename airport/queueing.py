from collections import deque
from .exceptions import EmptyQueueError
class CheckInQueue():
    def __init__(self):
        self._vip_queue = deque()
        self._regular_queue = deque()
    
    def enqueue(self, passenger):
        if passenger.is_vip:
            self._vip_queue.append(passenger)
        else:
            self._regular_queue.append(passenger)

    def next_passenger(self):
        if self._vip_queue:
            return self._vip_queue.popleft()
        elif self._regular_queue:
            return self._regular_queue.popleft()
        else:
            raise EmptyQueueError("The queue is empty. No passengers to serve.")
        
    def is_empty(self):
        return not (self._vip_queue or self._regular_queue)
