# Class representing the Round Robin CPU Scheduler
import time

from Job import Status
from LinearQueue import LinearQueue


class RoundRobinCPUScheduler(LinearQueue):
    def __init__(self, time_quantum):
        super().__init__()
        self.time_quantum = time_quantum
        self.tracked_jobs = []  # for tracking number of completed jobs
        self.total_context_switching_time = 0
        self.total_time_for_all_jobs_to_run = 0

    def process_jobs_round_robin(self, jobs, context_switching_time):
        time_quantum = self.time_quantum
        current_time = 0
        running_job = None
        cpu_available = True
        print(f"---------------------------------ROUND ROBIN START HERE------------------------------------------------")
        while jobs or not self.is_empty() or running_job:
            # Print the current time and queue status
            print(
                f"At time {current_time}: CPU available: {cpu_available}, Ready queue: {[job.job_number for job in self.ready_queue]}")

            # Add arriving jobs to the queue
            while jobs and jobs[0].arrival_time <= current_time:
                current_job = jobs.pop(0)
                self.enqueue(current_job)
                current_job.status = Status.READY
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
                print(f"Job memory size is: {running_job.memory_size}")
                print(f"Job status {running_job.status.value}")

            # Simulate job execution
            if running_job:
                minimum_execution_time = 1
                time.sleep(minimum_execution_time)
                running_job.remaining_time -= minimum_execution_time  # tracking remaining time
                running_job.running_time += minimum_execution_time

                # Update turn around time
                running_job.turn_around_time = running_job.exit_time - running_job.arrival_time

                # Update response time
                running_job.response_time = running_job.exit_time - running_job.arrival_time

                # Finish the job if execution is complete
                if running_job.remaining_time <= 0:
                    running_job.status = Status.EXIT
                    running_job.exit_time = current_time  # Update exit time
                    running_job.exit_time = running_job.exit_time + 1  # Update exit time
                    self.tracked_jobs.append(running_job)
                    cpu_available = True
                    print(f"Job status {running_job.status.value}")
                    print(f"-----------------finishing JOB {running_job.job_number}------------------")
                    running_job = None

                elif running_job.running_time >= time_quantum:
                    running_job.status = Status.READY
                    self.enqueue(running_job)
                    cpu_available = True
                    print(
                        f"At time {current_time + 1}: Time quantum expired for Job {running_job.job_number}. Putting back to ready queue.")
                    running_job = None

            current_time += 1
        print(f"---------------------------------ROUND ROBIN ENDS HERE------------------------------------------------")

        # print(f"Total context switching time is {self.total_context_switching_time}")
        self.total_time_for_all_jobs_to_run = self.tracked_jobs[-1].exit_time
        print(f"Total time is: {self.total_time_for_all_jobs_to_run}")

    def get_avg_wt(self):
        total_waiting_time = 0
        for job in self.tracked_jobs:
            total_waiting_time += (job.exit_time - job.arrival_time - job.actual_execution_time)
        average_waiting_time = total_waiting_time / len(self.tracked_jobs)
        return average_waiting_time

    def get_avg_turn_t(self):
        total_turnaround_time = 0
        for job in self.tracked_jobs:
            total_turnaround_time += (job.exit_time - job.arrival_time)
        average_turnaround_time = total_turnaround_time / len(self.tracked_jobs)
        return average_turnaround_time

    def get_cpu_utilization(self):
        if self.total_time_for_all_jobs_to_run == 0:
            return 0
        cpu_utilization = ((
                                       self.total_time_for_all_jobs_to_run - self.total_context_switching_time) / self.total_time_for_all_jobs_to_run) * 100
        return cpu_utilization

    def get_max_turn_around_time(self):
        max_turnaround_time = 0
        for job in self.tracked_jobs:
            turnaround_time = job.exit_time - job.arrival_time
            if turnaround_time > max_turnaround_time:
                max_turnaround_time = turnaround_time
        return max_turnaround_time

    def get_max_waiting_time(self):
        max_waiting_time = 0
        for job in self.tracked_jobs:
            waiting_time = job.exit_time - job.arrival_time - job.actual_execution_time
            if waiting_time > max_waiting_time:
                max_waiting_time = waiting_time
        return max_waiting_time

    def get_cpu_throughput(self):
        if self.total_time_for_all_jobs_to_run == 0:
            return 0
        throughput = len(self.tracked_jobs) / self.total_time_for_all_jobs_to_run
        return throughput
