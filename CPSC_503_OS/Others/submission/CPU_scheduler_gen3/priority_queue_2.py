import time

from Job import Status
from LinearQueue import LinearQueue
from Switch import Switch


class PriorityBased(LinearQueue):
    def __init__(self, switch):
        super().__init__()
        self.switch = switch
        self.aging_threshold = 1

    def process_jobs(self, job, context_switching_time , current_time_):
        if self.switch == Switch.NON_PREEMPTIVE:
            current_time = current_time_
            running_job = None
            cpu_available = True
            jobs = []
            jobs.append(job) #add job that has arrived to the list of jobs

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
                    print(
                        f"At time {current_time}: Running Job {running_job.job_number}, {running_job.remaining_time} time units remaining.")
                    minimum_execution_time = 1
                    time.sleep(minimum_execution_time)
                    running_job.remaining_time -= minimum_execution_time  # tracking remaining time


                    # Finish the job if execution is complete
                    if running_job.remaining_time <= 0:
                        running_job.status = Status.EXIT
                        cpu_available = True
                        print(f"Job status {running_job.status.value}")
                        print(f"-----------------finishing JOB {running_job.job_number}------------------")
                        running_job = None

                current_time += 1

        return current_time - 1  # Return the current time after processing jobs