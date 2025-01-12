import time
from Job import Status, Job
from LinearQueue import LinearQueue
from MemoryManager import MemoryManager


class FIFO(LinearQueue):
    def __init__(self):
        super().__init__()
        self.aging_threshold = 3  # Set aging threshold
        self.tracked_jobs = []  # for tracking number of completed jobs
        self.total_context_switching_time = 0
        self.total_time_for_all_jobs_to_run = 0

    def run_scheduler(self, jobs, context_switching_time=1):
        self.process_jobs_Fifo(jobs, context_switching_time)
        print(f"FIFO avg_turn_t is {self.get_avg_turn_t()}")
        print(f"FIFO avg_wt is {self.get_avg_wt()}")
        print(f"FIFO cpu utilization is {self.get_cpu_utilization()}%")
        print(f"FIFO Maximum turnaround time is {self.get_max_turn_around_time()}")
        print(f"FIFO Maximum wait time {self.get_max_waiting_time()}")
        print(f"FIFO CPU throughput is {self.get_cpu_throughput()}")

    def process_jobs_Fifo(self, jobs, context_switching_time):
        current_time = 0
        running_job = None
        cpu_available = True
        MM = MemoryManager(1)

        print(f"---------------------------------FIFO START HERE------------------------------------------------")
        # Process the first job outside the loop
        if jobs:
            current_job = jobs.pop(0)

            # Check if we have enough memory from a memory manager
            memory_is_available = MM.first_fit(current_job)

            print(f">>>>>>>>>>>>>>>>>Memory available: {memory_is_available} for job {current_job.job_number}")
            if memory_is_available:
                current_job.memory_needed = False
                current_job.status = Status.RUNNING
                running_job = current_job
                cpu_available = False
                print(
                    f"At time {current_time}: -----------------starting JOB {running_job.job_number}------------------")
                print(f"Job status {running_job.status.value}")
                minimum_execution_time = 1
                time.sleep(minimum_execution_time)
                running_job.remaining_time -= minimum_execution_time  # tracking remaining time
                running_job.running_time += minimum_execution_time

                if running_job.remaining_time <= 0:
                    MM.release_memory(running_job.job_number)  # releasing memory when job finishes executing
                    running_job.status = Status.EXIT
                    running_job.exit_time = current_time + 1  # Update exit time
                    self.tracked_jobs.append(running_job)
                    cpu_available = True
                    print(f"Job status {running_job.status.value}")
                    print(f"-----------------finishing JOB {running_job.job_number}------------------")
                    running_job = None

                current_time += 1

            elif not memory_is_available:
                current_job.memory_needed = True
                print(f">>>>>>>>>>>>>>>>>>>>Not enough memory for job {current_job.job_number}")
                if not any(job.job_number == current_job.job_number for job in self.ready_queue):
                    self.enqueue(current_job)  # add to ready queue to wait for memory
                    print(
                        f"At time {current_time}: job {current_job.job_number} added to ready queue to wait for memory. "
                        f"Ready queue: {[job.job_number for job in self.ready_queue]}")

        while jobs or not self.is_empty() or running_job:
            # Print the current time and queue status
            print(
                f"At time {current_time}: CPU available: {cpu_available}, "
                f"Ready queue: {[job.job_number for job in self.ready_queue]}")

            # Add arriving jobs to the queue
            while jobs and jobs[0].arrival_time <= current_time:
                current_job = jobs.pop(0)
                if not any(job.job_number == current_job.job_number for job in self.ready_queue):
                    self.enqueue(current_job)
                    print(f"At time {current_time}: Job {current_job.job_number} arrived and added to ready queue.")
                print(f" Ready queue: {[job.job_number for job in self.ready_queue]}")

            # Check if memory is available for any job in the ready queue
            if cpu_available:
                running_job = None
                for i in range(len(self.ready_queue)):
                    potential_job = self.ready_queue[i]
                    memory_is_available = MM.first_fit(potential_job)
                    if memory_is_available:
                        running_job = potential_job
                        running_job.memory_needed = False
                        del self.ready_queue[i]
                        break
                    elif not memory_is_available:
                        potential_job.memory_needed = True
                        print(f">>>>>>>>>>>>>>>>>>>>Not enough memory for job {potential_job.job_number}")

                if running_job:
                    current_time += context_switching_time
                    self.total_context_switching_time += context_switching_time
                    print(f"At time {current_time}: switching to Job {running_job.job_number}")
                    running_job.status = Status.RUNNING
                    cpu_available = False
                    print(f"-----------------starting JOB {running_job.job_number}------------------")
                    print(f"Job status {running_job.status.value}")

            # Simulate job execution
            if running_job:
                minimum_execution_time = 1
                time.sleep(minimum_execution_time)
                running_job.remaining_time -= minimum_execution_time  # tracking remaining time
                running_job.running_time += minimum_execution_time

                # Finish the job if execution is complete
                if running_job.remaining_time <= 0:
                    MM.release_memory(running_job.job_number)  # releasing memory when job finishes executing
                    running_job.status = Status.EXIT
                    running_job.exit_time = current_time + 1  # Update exit time
                    self.tracked_jobs.append(running_job)
                    cpu_available = True
                    print(f"Job status {running_job.status.value}")
                    print(f"-----------------finishing JOB {running_job.job_number}------------------")
                    running_job = None

            current_time += 1

            # Check if all jobs in the queue need memory and terminate the program to avoid infinite loop
            if self.all_jobs_need_memory() and not self.is_empty():
                print("All jobs in the queue need memory. Terminating the program.")
                exit()
                # continue

        print(f"---------------------------------FIFO ENDS HERE------------------------------------------------")

        self.total_time_for_all_jobs_to_run = self.tracked_jobs[-1].exit_time
        print(f"Total time is: {self.total_time_for_all_jobs_to_run}")

    def get_avg_wt(self):
        total_waiting_time = 0
        for job in self.tracked_jobs:
            total_waiting_time += (job.exit_time - job.arrival_time - job.actual_execution_time)
            print(f"job is {job}")
        average_waiting_time = total_waiting_time / len(self.tracked_jobs)
        return average_waiting_time

    def get_avg_turn_t(self):
        total_turnaround_time = 0
        for job in self.tracked_jobs:
            total_turnaround_time += (job.exit_time - job.arrival_time)
            # print(f"job is {job}")
        average_turnaround_time = total_turnaround_time / len(self.tracked_jobs)
        return average_turnaround_time

    def get_cpu_utilization(self):
        cpu_utilization = ((self.total_time_for_all_jobs_to_run - self.total_context_switching_time) / (
            self.total_time_for_all_jobs_to_run)) * 100
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
        throughput = len(self.tracked_jobs) / self.total_time_for_all_jobs_to_run
        return throughput

    def plot_optimization(self, jobs):
        pass
