# Class representing a linear queue
from collections import deque

from Job import Status


class LinearQueue:
    def __init__(self):
        self.ready_queue = deque()
        self.aging_threshold = 0  # Default aging threshold

    def enqueue(self, job):
        job.status = Status.READY
        # if not job.memory_needed:
        #     # Remove the job if it already exists in the queue
        #     self.ready_queue = deque([j for j in self.ready_queue if j != job])
        #     # Add the job to the front of the queue
        #     self.ready_queue.appendleft(job)
        # else:
        #     self.ready_queue.append(job)
        self.ready_queue.append(job)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.ready_queue.popleft()

    def is_empty(self):
        return len(self.ready_queue) == 0

    def add_to_front(self, job):
        self.ready_queue.appendleft(job)

    def all_jobs_need_memory(self):
        return all(job.memory_needed for job in self.ready_queue)