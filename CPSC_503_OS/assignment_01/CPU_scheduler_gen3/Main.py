from CPU_scheduler import MultiLevelQueueScheduling
from Job import Job, Status
from Switch import Switch

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

    context_switching_time = int(input(f"Enter Context Switching Time(should be integer): "))
    priority_based_switch_type_selection = int(input(f"Enter Switch type (1 for Non Pre-emptive , 2 for Pre-emptive): "))

    if priority_based_switch_type_selection == 1:
        switch = Switch.NON_PREEMPTIVE
    elif priority_based_switch_type_selection == 2:
        switch = Switch.PREEMPTIVE

    mlq = MultiLevelQueueScheduling()
    mlq.runMLQ(switch, jobs, context_switching_time)

    # mlq.plot_optimization(jobs)


if __name__ == "__main__":
    main()