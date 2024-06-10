# Class representing a priority-based queue
import time
import Switch
from Job import Status
from LinearQueue import LinearQueue


class PriorityBased(LinearQueue):
    def __init__(self, switch):
        super().__init__()
        self.switch = switch
        self.aging_threshold = 1

    def process_jobs(self, jobs, context_switching_time , current_time_):
        if self.switch == Switch.NON_PREEMPTIVE:
            current_time = current_time_
            running_job = None
            cpu_available = True

            # Process job1 first if it exists
            job1 = next((job for job in jobs if job.job_number == 1), None)
            if job1:
                jobs.remove(job1)
                job1.status = Status.RUNNING
                running_job = job1
                cpu_available = False
                print(
                    f"At time {current_time}: -----------------starting JOB {running_job.job_number}------------------")
                print(f"Job status {running_job.status.value}")
                print(
                    f"At time {current_time}: Running Job {running_job.job_number}, {running_job.remaining_time} time units remaining.")
                execution_time = min(running_job.remaining_time, 1)
                time.sleep(execution_time)
                running_job.remaining_time -= execution_time
                print(
                    f"At time {current_time + 1}: Running Job {running_job.job_number}, {running_job.remaining_time} time units remaining.")

                if running_job.remaining_time <= 0:
                    running_job.status = Status.EXIT
                    cpu_available = True
                    print(f"Job status {running_job.status.value}")
                    print(f"-----------------finishing JOB {running_job.job_number}------------------")
                    running_job = None

                current_time += 1

            # Sort jobs by priority
            jobs.sort(key=lambda x: x.priority)

            while jobs or not self.is_empty() or running_job:
                # Print the current time and queue status
                print(
                    f"At time {current_time}: CPU available: {cpu_available}, Ready queue: {[job.job_number for job in self.ready_queue]}")

                # Add arriving jobs to the queue
                while jobs and jobs[0].arrival_time <= current_time:
                    current_job = jobs.pop(0)
                    self.enqueue(current_job)
                    print(f"At time {current_time}: Job {current_job.job_number} arrived and added to ready queue.")
                    print(f"Ready queue: {[job.job_number for job in self.ready_queue]}")

                # Execute the job if CPU is available
                if cpu_available and not self.is_empty():
                    running_job = self.dequeue()
                    current_time += context_switching_time
                    print(f"At time {current_time}: switching to Job {running_job.job_number}")
                    running_job.status = Status.RUNNING
                    cpu_available = False
                    print(f"-----------------starting JOB {running_job.job_number}------------------")
                    print(f"Job status {running_job.status.value}")

                # Simulate job execution
                if running_job:
                    execution_time = min(running_job.remaining_time, 1)
                    time.sleep(execution_time)
                    running_job.remaining_time -= execution_time
                    print(
                        f"At time {current_time + 1}: Running Job {running_job.job_number}, {running_job.remaining_time} time units remaining.")

                    # Finish the job if execution is complete
                    if running_job.remaining_time <= 1:
                        running_job.status = Status.EXIT
                        running_job.exit_time = current_time  # Update exit time
                        running_job.exit_time = running_job.exit_time + 1  # Update exit time
                        cpu_available = True
                        print(f"Job status {running_job.status.value}")
                        print(f"-----------------finishing JOB {running_job.job_number}------------------")
                        running_job = None

                current_time += 1

        else:
            current_time = current_time_
            running_job = None
            cpu_available = True

            while jobs or not self.is_empty() or running_job:
                # Print the current time and queue status
                print(
                    f"At time {current_time}: CPU available: {cpu_available}, Ready queue: {[job.job_number for job in self.ready_queue]}")

                # Add arriving jobs to the queue
                while jobs and jobs[0].arrival_time <= current_time:
                    current_job = jobs.pop(0)
                    self.enqueue(current_job)
                    print(f"At time {current_time}: Job {current_job.job_number} arrived and added to ready queue.")
                    print(f"Ready queue: {[job.job_number for job in self.ready_queue]}")

                # Preemptive handling: check if a new job with higher priority should preempt the current job
                if running_job and not self.is_empty():
                    highest_priority_job = min(self.ready_queue, key=lambda job: job.priority)
                    if highest_priority_job.priority < running_job.priority:
                        self.enqueue(running_job)
                        running_job.status = Status.READY
                        running_job = highest_priority_job
                        self.ready_queue.remove(highest_priority_job)
                        running_job.status = Status.RUNNING
                        cpu_available = False
                        print(f"-----------------preempting JOB {running_job.job_number}------------------")
                        print(f"Job status {running_job.status.value}")

                # Execute the job if CPU is available
                if cpu_available and not self.is_empty():
                    running_job = self.dequeue()
                    current_time += context_switching_time
                    print(f"At time {current_time}: switching to Job {running_job.job_number}")
                    running_job.status = Status.RUNNING
                    cpu_available = False
                    print(f"-----------------starting JOB {running_job.job_number}------------------")
                    print(f"Job status {running_job.status.value}")

                # Simulate job execution
                if running_job:
                    execution_time = min(running_job.remaining_time, 1)
                    time.sleep(execution_time)
                    running_job.remaining_time -= execution_time
                    print(
                        f"At time {current_time + 1}: Running Job {running_job.job_number}, {running_job.remaining_time} time units remaining.")

                    # Finish the job if execution is complete
                    if running_job.remaining_time <= 0:
                        running_job.status = Status.EXIT
                        running_job.exit_time = current_time  # Update exit time
                        running_job.exit_time = running_job.exit_time + 1  # Update exit time
                        cpu_available = True
                        print(f"Job status {running_job.status.value}")
                        print(f"-----------------finishing JOB {running_job.job_number}------------------")
                        running_job = None

                current_time += 1

        return current_time  # Return the current time after processing jobs