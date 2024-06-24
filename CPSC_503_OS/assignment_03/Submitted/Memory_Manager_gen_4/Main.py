from FIFOScheduler import FIFO
from Job import Job, Status
from MemorySizes import MemorySizes
from Plot import Plot


def main():
    MS = MemorySizes()
    jobs = []
    job1 = Job(1, 0.0, 10, 3, 1, Status.CREATED, MS.get_memory_size("1MB"))
    jobs.append(job1)
    job2 = Job(2, 2, 1, 2, 1, Status.CREATED, MS.get_memory_size("129KB"))
    jobs.append(job2)
    job3 = Job(3, 4, 3.0, 1, 1, Status.CREATED, MS.get_memory_size("2MB"))
    jobs.append(job3)
    job4 = Job(4, 8, 5, 5, 1, Status.CREATED , MS.get_memory_size("512KB"))
    jobs.append(job4)
    job5 = Job(5, 12, 2, 4, 1, Status.CREATED, MS.get_memory_size("256KB"))
    jobs.append(job5)

    # Create separate lists for job 2 and job 3
    # jobs_2 = jobs.copy()
    # jobs_3 = jobs_2.copy()

    jobs_2 = []
    job1 = Job(1, 0.0, 10, 3, 1, Status.CREATED, MS.get_memory_size("1MB"))
    jobs_2.append(job1)
    job2 = Job(2, 2, 1, 2, 1, Status.CREATED, MS.get_memory_size("129KB"))
    jobs_2.append(job2)
    job3 = Job(3, 4, 3.0, 1, 1, Status.CREATED, MS.get_memory_size("9MB"))
    jobs_2.append(job3)
    job4 = Job(4, 8, 5, 5, 1, Status.CREATED , MS.get_memory_size("512KB"))
    jobs_2.append(job4)
    job5 = Job(5, 12, 2, 4, 1, Status.CREATED, MS.get_memory_size("256KB"))
    jobs_2.append(job5)


    # print(f"1. First Fit\n2. Best Fit\n3. Worst Fit")
    # fitting_algorithm = int(input(f"Selecting fitting algorithm from above(Enter number): "))

    # context_switching_time = int(input(f"Enter Context Switching Time(should be integer): "))
    # context_switching_time = 0

    metrics_list = []

    content_switching_times = [0, 1 , 2]

    # for context_switching_time in content_switching_times:
    #     fifo = FIFO()
    #     metrics = fifo.run_scheduler(jobs, context_switching_time)
    #     metrics_list.extend(metrics)

    fifo = FIFO()
    metrics = fifo.run_scheduler(jobs, content_switching_times[0])
    metrics_list.extend(metrics)

    # fifo1 = FIFO()
    # metrics = fifo1.run_scheduler(jobs_2, content_switching_times[0])
    # metrics_list.extend(metrics)

    # fifo2 = FIFO()
    # metrics = fifo2.run_scheduler(jobs_3, content_switching_times[2])
    # metrics_list.extend(metrics)

    # fifo = FIFO()
    # metrics_list = fifo.run_scheduler(jobs, context_switching_time)

    # print(f"metrics_list: {metrics_list[0]}")

    # plotting
    my_plot = Plot()  # Create an instance ofPlot.
    # my_plot.plot_optimization(metrics_list)

    my_plot.plot_fragmentation_metrics(fifo.fragmentation_metrics)


if __name__ == "__main__":
    main()
