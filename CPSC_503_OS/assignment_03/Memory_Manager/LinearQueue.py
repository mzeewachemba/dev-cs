# Class representing a linear queue
from collections import deque

from Job import Status


class LinearQueue:
    def __init__(self):
        self.ready_queue = deque()
        self.aging_threshold = 0  # Default aging threshold

    def enqueue(self, job):
        job.status = Status.READY
        self.ready_queue.append(job)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.ready_queue.popleft()

    def is_empty(self):
        return len(self.ready_queue) == 0