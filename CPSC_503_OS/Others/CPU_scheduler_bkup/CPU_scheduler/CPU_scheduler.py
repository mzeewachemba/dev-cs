import sys
from Job import Job
from LinearQueue import LinearQueue
from Status import Status
from FIFO import FIFO


def main():
    jobs = []
    job1 = Job(1, 0.0, 10, 3, 1, Status.CREATED)
    jobs.append(job1)
    job2 = Job(2, 2, 1, 2, 2, Status.CREATED)
    jobs.append(job2)
    job3 = Job(3, 4, 3.0, 1, 3, Status.CREATED)
    jobs.append(job3)
    job4 = Job(4, 8, 5, 5, 1, Status.CREATED)
    jobs.append(job4)
    job5 = Job(5, 12, 2, 4, 2, Status.CREATED)
    jobs.append(job5)

    aging_threshold = 1
    linear_queue = LinearQueue(aging_threshold)
    fifo = FIFO(linear_queue)

    for i in range(len(jobs)):
        print(f"-----------------starting JOB {i}------------------")
        fifo.process_job(jobs[i])
        print(f"-----------------finishing JOB {i}------------------")


if __name__ == "__main__":
    sys.exit(int(main() or 0))