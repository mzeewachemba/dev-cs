from enum import Enum
from collections import deque
import time
import matplotlib.pyplot as plt
from Job import Status, Job
from LinearQueue import LinearQueue
from Switch import Switch
from priority_queue_2 import PriorityBased

class MultiLevelQueueScheduling(LinearQueue):
    def __init__(self):
        super().__init__()
        self.aging_threshold = 3  # Set aging threshold
        self.transfer_job = None  # List to store transferred jobs
        self.tracked_jobs = []  # for tracking number of completed jobs
        self.total_context_switching_time = 0
        self.total_time_for_all_jobs_to_run = 0

    def runMLQ(self, priority_based_switch, jobs, context_switching_time):
        self.process_jobs_Fifo(jobs, context_switching_time, priority_based_switch)
        print(f"FIFO avg_turn_t is {self.get_avg_turn_t()}")
        print(f"FIFO avg_wt is {self.get_avg_wt()}")
        print(f"FIFO cpu utilization is {self.get_cpu_utilization()}%")
        print(f"FIFO Maximum turnaround time is {self.get_max_turn_around_time()}")
        print(f"FIFO Maximum wait time {self.get_max_waiting_time()}")
        print(f"FIFO CPU throughput is {self.get_cpu_throughput()}")

    def process_jobs_Fifo(self, jobs, context_switching_time, priority_based_switch):
        current_time = 0
        running_job = None
        cpu_available = True
        print(f"---------------------------------FIFO START HERE------------------------------------------------")
        # Process the first job outside the loop
        if jobs:
            current_job = jobs.pop(0)
            current_job.status = Status.RUNNING
            running_job = current_job
            cpu_available = False
            print(f"At time {current_time}: -----------------starting JOB {running_job.job_number}------------------")
            print(f"Job status {running_job.status.value}")
            minimum_execution_time = 1
            time.sleep(minimum_execution_time)
            running_job.remaining_time -= minimum_execution_time  # tracking remaining time
            running_job.running_time += minimum_execution_time
            print(
                f"At time {current_time + 1}: Running Job {running_job.job_number}, {running_job.remaining_time} time units remaining.")

            if running_job.remaining_time <= 0:
                running_job.status = Status.EXIT
                cpu_available = True
                print(f"Job status {running_job.status.value}")
                print(f"-----------------finishing JOB {running_job.job_number}------------------")
                running_job = None

            current_time += 1

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
                minimum_execution_time = 1
                time.sleep(minimum_execution_time)
                running_job.remaining_time -= minimum_execution_time  # tracking remaining time
                running_job.running_time += minimum_execution_time
                if running_job.running_time < self.aging_threshold:
                    print(
                        f"At time {current_time + 1}: Running Job {running_job.job_number}, {running_job.remaining_time} time units remaining.")

                # time_before_switch = current_time
                # 
                # # Transfer the job if it exceeds the aging threshold
                # if running_job.running_time > self.aging_threshold:
                #     running_job.status = Status.READY
                #     running_job.remaining_time = running_job.actual_execution_time - time_before_switch
                #     print(
                #         f"At time {current_time + 1}: Job {running_job.job_number} exceeded aging threshold and transferred.")
                #     self.transfer_job = running_job
                #     current_time = self.process_jobs_priority_based(priority_based_switch, context_switching_time,
                #                                                     current_time + 1)
                #     running_job = None
                #     cpu_available = True

                # Finish the job if execution is complete
                # elif running_job.remaining_time <= 0:
                if running_job.remaining_time <= 0:
                    running_job.status = Status.EXIT
                    running_job.exit_time = current_time  # Update exit time
                    running_job.exit_time = running_job.exit_time + 1  # Update exit time
                    self.tracked_jobs.append(running_job)
                    cpu_available = True
                    print(f"Job status {running_job.status.value}")
                    print(f"-----------------finishing JOB {running_job.job_number}------------------")
                    running_job = None

            current_time += 1
        print(f"---------------------------------FIFO ENDS HERE------------------------------------------------")

        # print(f"Total context switching time is {self.total_context_switching_time}")
        self.total_time_for_all_jobs_to_run = self.tracked_jobs[-1].exit_time
        print(f"Total time is: {self.total_time_for_all_jobs_to_run}")

    def process_jobs_priority_based(self, priority_based_switch, context_switching_time, current_time):
        print(f"---------------------------------PRIORITY BASED START HERE-----------------------------------------")

        if priority_based_switch == Switch.NON_PREEMPTIVE:
            priority = PriorityBased(priority_based_switch)
            current_time = priority.process_jobs(self.transfer_job, context_switching_time, current_time)

        elif priority_based_switch == Switch.PREEMPTIVE:
            priority = PriorityBased(priority_based_switch)
            current_time = priority.process_jobs(self.transfer_job, context_switching_time, current_time)

        print(f"---------------------------------PRIORITY BASED ENDS HERE------------------------------------------")
        return current_time

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
        cpu_utilization = ((self.total_time_for_all_jobs_to_run - self.total_context_switching_time)/(self.total_time_for_all_jobs_to_run)) * 100
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
        context_switching_time_list = [0, 1, 2, 3, 0.2]
        priority_based_switch = Switch.NON_PREEMPTIVE
        plt.figure(figsize=(12, 8))

        markers = ['o', '+', '^', 'D', '.', '*']  # Different markers for each plot

        # time = context_switching_time_list[0]
        # time = context_switching_time_list[1]
        # time = context_switching_time_list[2]
        # time = context_switching_time_list[3]
        # time = context_switching_time_list[4]

        self.process_jobs_Fifo(jobs, time, priority_based_switch)
        avg_turnaround_times = self.get_avg_turn_t()
        avg_waiting_times = self.get_avg_wt()
        cpu_utilizations = self.get_cpu_utilization()
        max_turnaround_times = self.get_max_turn_around_time()
        max_waiting_times = self.get_max_waiting_time()
        cpu_throughputs = self.get_cpu_throughput()

        print(f"FIFO avg_turn_t is {self.get_avg_turn_t()}")
        print(f"FIFO avg_wt is {self.get_avg_wt()}")
        print(f"FIFO cpu utilization is {self.get_cpu_utilization()}%")
        print(f"FIFO Maximum turnaround time is {self.get_max_turn_around_time()}")
        print(f"FIFO Maximum wait time {self.get_max_waiting_time()}")
        print(f"FIFO CPU throughput is {self.get_cpu_throughput()}")

        # Plot avg_turnaround_times
        plt.plot(time, avg_turnaround_times, label=f'Avg Turnaround Time ({time} s)', marker=markers[0])

        # Plot avg_waiting_times
        plt.plot(time, avg_waiting_times, label=f'Avg Waiting Time ({time} s)', marker=markers[1])

        # Plot cpu_utilizations
        plt.plot(time, cpu_utilizations, label=f'CPU Utilization ({time} s)', marker=markers[2])

        # Plot max_turnaround_times
        plt.plot(time, max_turnaround_times, label=f'Max Turnaround Time ({time} s)', marker=markers[3])

        # Plot max_waiting_times
        plt.plot(time, max_waiting_times, label=f'Max Waiting Time ({time} s)', marker=markers[4])

        # Plot cpu_throughputs
        plt.plot(time, cpu_throughputs, label=f'CPU Throughput ({time} s)', marker=markers[5])

        # Annotate numerical values on the graph
        plt.annotate(f'{avg_turnaround_times:.2f}', (time, avg_turnaround_times), textcoords="offset points",
                     xytext=(0, 10), ha='center')
        plt.annotate(f'{avg_waiting_times:.2f}', (time, avg_waiting_times), textcoords="offset points", xytext=(0, 10),
                     ha='center')
        plt.annotate(f'{cpu_utilizations:.2f}%', (time, cpu_utilizations), textcoords="offset points", xytext=(0, 10),
                     ha='center')
        plt.annotate(f'{max_turnaround_times:.2f}', (time, max_turnaround_times), textcoords="offset points",
                     xytext=(0, 10), ha='center')
        plt.annotate(f'{max_waiting_times:.2f}', (time, max_waiting_times), textcoords="offset points", xytext=(0, 10),
                     ha='center')
        plt.annotate(f'{cpu_throughputs:.2f}', (time, cpu_throughputs), textcoords="offset points", xytext=(0, 10),
                     ha='center')

        plt.xlabel('Context Switching Time (s)')
        plt.ylabel('Metrics')
        plt.title('Metrics vs Context Switching Time')
        plt.legend()
        plt.grid(True)
        plt.show()