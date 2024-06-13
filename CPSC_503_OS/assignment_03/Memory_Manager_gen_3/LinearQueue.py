# Class representing a linear queue
from collections import deque

from Job import Status


class LinearQueue:
    def __init__(self):
        self.ready_queue = deque()
        self.aging_threshold = 0  # Default aging threshold

    def enqueue(self, job):
        job.status = Status.READY
        # self.ready_queue.append(job)
        if job.memory_needed:
            self.ready_queue.appendleft(job)
        else:
            self.ready_queue.append(job)
        # self.ready_queue.append(job)
        self.update_queue_for_memory()

    def dequeue(self):
        if self.is_empty():
            return None
        return self.ready_queue.popleft()

    def is_empty(self):
        return len(self.ready_queue) == 0

    def update_queue_for_memory(self):
        non_memory_jobs = [job for job in self.ready_queue if not job.memory_needed]
        for job in non_memory_jobs:
            self.ready_queue.remove(job)
            self.ready_queue.appendleft(job)
