from enum import Enum
from collections import deque
import time
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
        self.remaining_time = actual_execution_time

    def __str__(self):
        return f"Job #{self.job_number} - Arrival: {self.arrival_time:.2f}, Execution Time: {self.actual_execution_time:.2f}, Priority: {self.priority}, Queue: {self.queue_number}, Status: {self.status}"

class Switch(Enum):
    PREEMPTIVE = "preemptive_scheduling"
    NON_PREEMPTIVE = "non_preemptive_scheduling"

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

class FIFO(LinearQueue):
    def __init__(self, aging_threshold):
        super().__init__()
        self.aging_threshold = aging_threshold

    def process_jobs(self, jobs):
        current_time = 0
        running_job = None
        cpu_available = True

        while jobs or not self.is_empty() or running_job:
            # Print the current time at each iteration
            print(f"At time {current_time}: CPU available: {cpu_available}, Ready queue: {[job.job_number for job in self.ready_queue]}")

            while jobs and jobs[0].arrival_time <= current_time:
                current_job = jobs.pop(0)
                self.enqueue(current_job)
                print(f"At time {current_time}: Job {current_job.job_number} arrived and added to ready queue.")
                print(f"Ready queue: {[job.job_number for job in self.ready_queue]}")

            if cpu_available and not self.is_empty():
                running_job = self.dequeue()
                running_job.status = Status.RUNNING
                cpu_available = False
                print(f"-----------------starting JOB {running_job.job_number}------------------")
                print(f"Job status {running_job.status.value}")

            if running_job:
                execution_time = min(running_job.remaining_time, 1)  # Simulate job execution for 1 time unit
                time.sleep(execution_time)
                running_job.remaining_time -= execution_time
                print(f"At time {current_time + 1}: Running Job {running_job.job_number}, {running_job.remaining_time} time units remaining.")

                if running_job.remaining_time <= 0:
                    running_job.status = Status.EXIT
                    cpu_available = True
                    print(f"Job status {running_job.status.value}")
                    print(f"-----------------finishing JOB {running_job.job_number}------------------")
                    running_job = None

            current_time += 1
            
class PriorityBased(LinearQueue):
    """
    This class represents a priority-based queue.
    """
    def __init__(self, aging_threshold, switch):
        super().__init__()
        self.switch = switch

    def process_jobs(self, jobs):
        current_time = 0
        running_job = None
        cpu_available = True
        
        # Remove the first job
        first_job = jobs.pop(0) if jobs else None

        # Sort jobs by their arrival time (second variable)
        jobs.sort(key=lambda x: x.priority)

        while jobs or not self.is_empty() or running_job:
            # Print the current time at each iteration
            print(f"At time {current_time}: CPU available: {cpu_available}, Ready queue: {[job.job_number for job in self.ready_queue]}")

            # Add jobs from the list to the ready queue based on their arrival time
            while jobs and jobs[0].arrival_time <= current_time:
                current_job = jobs.pop(0)
                self.enqueue(current_job)
                print(f"At time {current_time}: Job {current_job.job_number} arrived and added to ready queue.")
                print(f"Ready queue: {[job.job_number for job in self.ready_queue]}")

            if cpu_available and not self.is_empty():
                running_job = self.dequeue()
                running_job.status = Status.RUNNING
                cpu_available = False
                print(f"-----------------starting JOB {running_job.job_number}------------------")
                print(f"Job status {running_job.status.value}")

            if running_job:
                execution_time = min(running_job.remaining_time, 1)  # Simulate job execution for 1 time unit
                time.sleep(execution_time)
                running_job.remaining_time -= execution_time
                print(f"At time {current_time + 1}: Running Job {running_job.job_number}, {running_job.remaining_time} time units remaining.")

                if running_job.remaining_time <= 0:
                    running_job.status = Status.EXIT
                    cpu_available = True
                    print(f"Job status {running_job.status.value}")
                    print(f"-----------------finishing JOB {running_job.job_number}------------------")
                    running_job = None

            current_time += 1

        

def main():
    jobs = []
    job1 = Job(1, 0.0, 10, 3, 1, Status.CREATED)
    jobs.append(job1)
    job2 = Job(2, 2, 1, 2, 2, Status.CREATED)
    jobs.append(job2)
    job3 = Job(3, 4, 3.0, 1, 3, Status.CREATED)
    jobs.append(job3)
    job4 = Job(4, 8, 5, 5, 1, Status.CREATED)
    jobs.append(job4)
    job5 = Job(5, 12, 2, 4, 2, Status.CREATED)
    jobs.append(job5)

    # aging_threshold_fifo = 1
    # fifo = FIFO(aging_threshold_fifo)
    # fifo.process_jobs(jobs)
    
    aging_threshold_fifo = 1
    switch = Switch.NON_PREEMPTIVE
    priority = PriorityBased(aging_threshold_fifo , switch)
    priority.process_jobs(jobs)

    # Add code for other queues (PriorityBased, SJF, Round Robin) here

def generate_jobs(num_jobs):
    jobs = []
    for i in range(1, num_jobs + 1):
        arrival_time = random.uniform(0, 20)  # Random arrival time
        execution_time = random.uniform(1, 10)  # Random execution time
        priority = random.randint(1, 5)  # Random priority
        queue_number = random.randint(1, 4)  # Random queue number
        status = Status.CREATED
        job = Job(i, arrival_time, execution_time, priority, queue_number, status)
        jobs.append(job)
    return jobs

if __name__ == "__main__":
    main()
