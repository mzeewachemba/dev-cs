from enum import Enum
import random

class Status(Enum):
    CREATED = "created"
    READY = "ready"
    RUNNING = "Running"
    EXIT = "exit"

# Class to represent a job

class Job:
    def __init__(self, job_number, arrival_time, actual_execution_time, priority, queue_number, status):
        self.job_number = job_number
        self.arrival_time = arrival_time
        self.actual_execution_time = actual_execution_time
        self.priority = priority
        self.queue_number = queue_number
        self.status = status
        self.remaining_time = actual_execution_time #intialize remaining time as actual execution time for each job
        self.running_time = 0  # Track running time
        self.exit_time = 0
        self.turn_around_time = 0

    def __str__(self):
        return (f"Job #{self.job_number} - Arrival: {self.arrival_time:.2f}, "
                f"Execution Time: {self.actual_execution_time:.2f}, Priority: {self.priority}, "
                f"Queue: {self.queue_number}, Status: {self.status.value} ,Remaining time: {self.remaining_time},"
                f"Exit time: {self.exit_time} , Turn Around Time: {self.turn_around_time}")