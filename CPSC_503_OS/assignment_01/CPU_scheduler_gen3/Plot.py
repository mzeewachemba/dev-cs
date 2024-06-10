from CPU_scheduler import MultiLevelQueueScheduling
from Job import Job, Status
from Switch import Switch
import matplotlib.pyplot as plt


class Plot:
    def __init__(self):
        pass

    def plot_optimization(self, jobs):
        context_switching_time_list = [0, 1, 2, 0.1, 0.2]
        priority_based_switch = Switch.NON_PREEMPTIVE
        markers = ['o', '+', '^', 'D', '.', '*']  # Different markers for each plot

        # Plot CPU Utilization in its own plot
        plt.figure(figsize=(12, 8))
        for time in context_switching_time_list:
            mlq = MultiLevelQueueScheduling()
            mlq.process_jobs_Fifo(jobs, time, priority_based_switch)
            cpu_utilizations = mlq.get_cpu_utilization()
            plt.plot(time, cpu_utilizations, label=f'CPU Utilization ({time} s)', marker=markers[2])

        plt.xlabel('Context Switching Time (s)')
        plt.ylabel('CPU Utilization (%)')
        plt.title('CPU Utilization vs Context Switching Time')
        plt.legend()
        plt.grid(True)
        plt.show()

        # Plot other metrics in a combined plot
        plt.figure(figsize=(12, 8))
        for time in context_switching_time_list:
            mlq = MultiLevelQueueScheduling()
            mlq.process_jobs_Fifo(jobs, time, priority_based_switch)
            avg_turnaround_times = self.get_avg_turn_t()
            avg_waiting_times = self.get_avg_wt()
            max_turnaround_times = self.get_max_turn_around_time()
            max_waiting_times = self.get_max_waiting_time()
            cpu_throughputs = self.get_cpu_throughput()

            # Plot avg_turnaround_times
            plt.plot(time, avg_turnaround_times, label=f'Avg Turnaround Time ({time} s)', marker=markers[0])

            # Plot avg_waiting_times
            plt.plot(time, avg_waiting_times, label=f'Avg Waiting Time ({time} s)', marker=markers[1])

            # Plot max_turnaround_times
            plt.plot(time, max_turnaround_times, label=f'Max Turnaround Time ({time} s)', marker=markers[3])

            # Plot max_waiting_times
            plt.plot(time, max_waiting_times, label=f'Max Waiting Time ({time} s)', marker=markers[4])

            # Plot cpu_throughputs
            plt.plot(time, cpu_throughputs, label=f'CPU Throughput ({time} s)', marker=markers[5])

            # Annotate numerical values on the graph
            plt.annotate(f'{avg_turnaround_times:.2f}', (time, avg_turnaround_times), textcoords="offset points",
                         xytext=(0, 10), ha='center')
            plt.annotate(f'{avg_waiting_times:.2f}', (time, avg_waiting_times), textcoords="offset points",
                         xytext=(0, 10),
                         ha='center')
            plt.annotate(f'{max_turnaround_times:.2f}', (time, max_turnaround_times), textcoords="offset points",
                         xytext=(0, 10), ha='center')
            plt.annotate(f'{max_waiting_times:.2f}', (time, max_waiting_times), textcoords="offset points",
                         xytext=(0, 10),
                         ha='center')
            plt.annotate(f'{cpu_throughputs:.2f}', (time, cpu_throughputs), textcoords="offset points", xytext=(0, 10),
                         ha='center')

        plt.xlabel('Context Switching Time (s)')
        plt.ylabel('Metrics')
        plt.title('Metrics vs Context Switching Time')
        plt.legend()
        plt.grid(True)
        plt.show()

def main():
    global switch
    jobs = []
    job1 = Job(1, 0.0, 10, 3, 1, Status.CREATED)
    jobs.append(job1)
    job2 = Job(2, 2, 1, 2, 1, Status.CREATED)
    jobs.append(job2)
    job3 = Job(3, 4, 3.0, 1, 1, Status.CREATED)
    jobs.append(job3)
    job4 = Job(4, 8, 5, 5, 1, Status.CREATED)
    jobs.append(job4)
    job5 = Job(5, 12, 2, 4, 1, Status.CREATED)
    jobs.append(job5)

    plt = Plot()
    plt.plot_optimization(jobs)


if __name__ == "__main__":
    main()