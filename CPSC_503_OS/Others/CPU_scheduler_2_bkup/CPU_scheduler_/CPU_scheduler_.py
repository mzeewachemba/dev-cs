from enum import Enum
from collections import deque
import time
import random
from Job import Job,Status

class Switch(Enum):
    PREEMPTIVE = "preemptive_scheduling"
    NON_PREEMPTIVE = "non_preemptive_scheduling"

class LinearQueue:
    def __init__(self):
        self.ready_queue = deque()
        self.aging_threshold = 0  # Default aging threshold

    def enqueue(self, job):
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
        while jobs:
            current_job = jobs.pop(0)
            if current_job.arrival_time > current_time:
                print(f"At time {current_time}: No jobs arrived.")
                time.sleep(current_job.arrival_time - current_time)
                current_time = current_job.arrival_time
            print(f"At time {current_time}: Job {current_job.job_number} arrived.")
            self.enqueue(current_job)
            current_time += current_job.context_switch_time #switching from one job to the other
            self.execute_jobs(current_time)

    def execute_jobs(self, current_time):
        while not self.is_empty():
            job = self.dequeue()
            print(f"At time {current_time}: Executing Job {job.job_number}.")
            time.sleep(job.actual_execution_time) #simulating executing the job
            current_time += job.actual_execution_time
            print(f"At time {current_time}: Job {job.job_number} completed.")

class PriorityBased(LinearQueue):
    def __init__(self, aging_threshold, switch):
        super().__init__()
        self.aging_threshold = aging_threshold
        self.switch = switch

    def process_jobs(self, jobs):
        current_time = 0
        while jobs:
            current_job = jobs.pop(0)
            if current_job.arrival_time > current_time:
                print(f"At time {current_time}: No jobs arrived.")
                time.sleep(current_job.arrival_time - current_time)
                current_time = current_job.arrival_time
            print(f"At time {current_time}: Job {current_job.job_number} arrived.")
            self.enqueue(current_job)
            current_time += current_job.context_switch_time
            self.execute_jobs(current_time)

    def execute_jobs(self, current_time):
        while not self.is_empty():
            job = self.dequeue()
            print(f"At time {current_time}: Executing Job {job.job_number}.")
            time.sleep(job.actual_execution_time)
            current_time += job.actual_execution_time
            print(f"At time {current_time}: Job {job.job_number} completed.")

# Define SJF and Round Robin classes similarly

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
    # jobs = generate_jobs(10)  # Generate 10 random jobs for testing
    aging_threshold_fifo = 1
    fifo = FIFO(aging_threshold_fifo)
    fifo.process_jobs(jobs)

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

