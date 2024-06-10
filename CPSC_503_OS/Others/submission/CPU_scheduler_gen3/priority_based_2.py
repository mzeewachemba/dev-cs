from enum import Enum

from Job import Status, Job
from Switch import Switch

class Scheduler:
    def __init__(self):
        self.ready_queue = []

    def add_job(self, job):
        self.ready_queue.append(job)
        self.ready_queue.sort(key=lambda x: x.priority, reverse=True)  # Sort by priority

    def execute_jobs(self, context_switching_time, current_time, mode):
        while self.ready_queue:
            job = self.ready_queue.pop(0)  # Get the highest priority job
            job.status = Status.RUNNING
            if mode == Switch.PREEMPTIVE:
                while job.remaining_time > 0:
                    current_time += 1
                    job.remaining_time -= 1
                    job.running_time += 1
                    # Simulate context switching
                    if self.ready_queue and current_time % context_switching_time == 0:
                        self.ready_queue.append(job)
                        self.ready_queue.sort(key=lambda x: x.priority, reverse=True)  # Sort by priority
                        job.status = Status.READY
                        break
            else:  # Non-preemptive mode
                current_time += job.remaining_time
                job.running_time += job.remaining_time
                job.remaining_time = 0

            job.status = Status.EXIT
            job.exit_time = current_time
            job.turn_around_time = job.exit_time - job.arrival_time
            print(f"Job {job.job_number} finished execution at time {current_time}")

        print("All jobs have finished execution.")

# Sample jobs
jobs = [
    Job(1, 0.0, 10, 3, 1, Status.CREATED),
    Job(2, 2, 1, 2, 1, Status.CREATED),
    Job(3, 4, 3.0, 1, 1, Status.CREATED),
    Job(4, 8, 5, 5, 1, Status.CREATED),
    Job(5, 12, 2, 4, 1, Status.CREATED)
]

# Create a scheduler and add jobs
scheduler = Scheduler()
for job in jobs:
    scheduler.add_job(job)

# Execute jobs in non-preemptive mode
# print("Executing jobs in non-preemptive mode:")
# scheduler.execute_jobs(context_switching_time=1, current_time=0, mode=Switch.NON_PREEMPTIVE)

# Execute jobs in preemptive mode
print("\nExecuting jobs in preemptive mode:")
scheduler.execute_jobs(context_switching_time=1, current_time=0, mode=Switch.PREEMPTIVE)
