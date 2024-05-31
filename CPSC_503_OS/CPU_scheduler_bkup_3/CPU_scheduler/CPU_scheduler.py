import sys
from Job import Job  # Assuming Job class is defined in Job.py
from LinearQueue import LinearQueue  # Assuming LinearQueue class is defined in LinearQueue.py
from Status import Status  # Assuming Status enum is defined in Status.py
from FIFO import FIFO
from Switch import Switch
from ShortJobFirst_SJF import ShortJobFirst_SJF
from PriorityBased import PriorityBased


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

    aging_threshold_fifo = 1
    fifo = FIFO(aging_threshold_fifo)
    jobs = fifo.sort_jobs_by_arrival_time(jobs)
    fifo.process_jobs(jobs)

    # aging_threshold_sjf = 2
    
    # switch = Switch.NON_PREEMPTIVE
    # sjf = (aging_threshold_sjf , switch)
    # jobs = sjf.sort_jobs_by_execution_time(jobs)
    # sjf.process_jobs(jobs)
        

    # aging_threshold_pb = 5
    
    # switch = Switch.NON_PREEMPTIVE
    # pb = PriorityBased(aging_threshold_pb , switch)
    # jobs = pb.sort_jobs_by_priority(jobs)
    # pb.process_jobs(jobs)


if __name__ == "__main__":
    sys.exit(int(main() or 0))
