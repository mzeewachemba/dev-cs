from FIFOScheduler import FIFO
from Job import Job, Status
from MemorySizes import MemorySizes


def main():
    MS = MemorySizes()
    jobs = []
    job1 = Job(1, 0.0, 10, 3, 1, Status.CREATED, MS.get_memory_size("2MB"))
    jobs.append(job1)
    job2 = Job(2, 2, 1, 2, 1, Status.CREATED, MS.get_memory_size("1MB"))
    jobs.append(job2)
    job3 = Job(3, 4, 3.0, 1, 1, Status.CREATED, MS.get_memory_size("128KB"))
    jobs.append(job3)
    job4 = Job(4, 8, 5, 5, 1, Status.CREATED , MS.get_memory_size("1MB"))
    jobs.append(job4)
    job5 = Job(5, 12, 2, 4, 1, Status.CREATED, MS.get_memory_size("1MB"))
    jobs.append(job5)

    # print(f"1. First Fit\n2. Best Fit\n3. Worst Fit")
    # fitting_algorithm = int(input(f"Selecting fitting algorithm from above(Enter number): "))

    # context_switching_time = int(input(f"Enter Context Switching Time(should be integer): "))
    context_switching_time = 0
    fifo = FIFO()
    fifo.run_scheduler(jobs, context_switching_time)

if __name__ == "__main__":
    main()