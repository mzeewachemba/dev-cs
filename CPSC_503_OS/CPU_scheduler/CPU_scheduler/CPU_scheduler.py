from calendar import c
import sys
from Job import Job
from Status import Status
from FIFO import FIFO

def main():
    job1 = Job(1, 0.0, 10, 3, 1 ,Status.CREATED)  
    job2 = Job(2, 2, 1, 2, 2,Status.CREATED)   
    job3 = Job(3, 4, 3.0, 1, 3,Status.CREATED) 
    job4 = Job(4, 8, 5, 5, 1,Status.CREATED) 
    job5 = Job(5, 12, 2, 4, 2,Status.CREATED)
    
    
    
    

if __name__ == "__main__":
    sys.exit(int(main() or 0))
