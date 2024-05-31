from enum import Enum
import random

class Status(Enum):
    CREATED = "created"
    READY = "ready"
    RUNNING = "Running"
    EXIT = "exit"

class Job:
    def __init__(self, job_number, arrival_time, actual_execution_time, priority, queue_number, status):
        self.job_number = job_number
        self.arrival_time = arrival_time
        self.actual_execution_time = actual_execution_time
        self.priority = priority
        self.queue_number = queue_number
        self.status = status
        # self.context_switch_time = random.randint(1, 5)  # Random context switching time
        self.context_switch_time = 0


    def __str__(self):
        return f"Job #{self.job_number} - Arrival: {self.arrival_time:.2f}, Execution Time: {self.actual_execution_time:.2f}, Priority: {self.priority}, Queue: {self.queue_number}, Status: {self.status}, Context Switch Time: {self.context_switch_time}"

