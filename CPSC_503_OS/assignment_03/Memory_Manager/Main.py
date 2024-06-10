from Job import Job, Status
from Round_robin_scheduler import RoundRobinCPUScheduler
from Memory_Sizes import MemorySizes


def main():
    MS = MemorySizes()
    jobs = []
    job1 = Job(1, 0.0, 5, 3, 1, Status.CREATED, MS.get_memory_size("4KB"))
    jobs.append(job1)
    job2 = Job(2, 2, 1, 2, 1, Status.CREATED, MS.get_memory_size("8KB"))
    jobs.append(job2)
    job3 = Job(3, 5, 3.0, 1, 1, Status.CREATED, MS.get_memory_size("10KB"))
    jobs.append(job3)
    # job4 = Job(4, 8, 5, 5, 1, Status.CREATED)
    # jobs.append(job4)
    # job5 = Job(5, 12, 2, 4, 1, Status.CREATED)
    # jobs.append(job5)

    # print(f"1. First Fit\n2. Best Fit\n3. Worst Fit")
    # fitting_algorithm = int(input(f"Selecting fitting algorithm from above(Enter number): "))

    scheduler = RoundRobinCPUScheduler(time_quantum=4)
    scheduler.process_jobs_round_robin(jobs, context_switching_time=0)


if __name__ == "__main__":
    main()
