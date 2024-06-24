class SchedulerMetrics:
    def __init__(self, name, avg_turn_t, avg_wt, cpu_utilization, max_turnaround_time, max_wait_time, cpu_throughput):
        self.name = name
        self.avg_turn_t = avg_turn_t
        self.avg_wt = avg_wt
        self.cpu_utilization = cpu_utilization
        self.max_turnaround_time = max_turnaround_time
        self.max_wait_time = max_wait_time
        self.cpu_throughput = cpu_throughput

    # print values
    def __str__(self):
        return f"Scheduler name: {self.name}\n" \
               f"Average Turnaround time: {self.avg_turn_t}\n" \
               f"Average Wait time: {self.avg_wt}\n" \
               f"CPU Utilization: {self.cpu_utilization}\n" \
               f"Maximum Turnaround Time: {self.max_turnaround_time}\n" \
               f"Maximum Wait Time: {self.max_wait_time}\n" \
               f"CPU Throughput: {self.cpu_throughput}\n"