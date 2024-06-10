from Chronometer import Chronometer
from Status import Status
from LinearQueue import LinearQueue

class FIFO(LinearQueue):
  """
  This class represents a linear queue with an aging threshold.
  """
  def __init__(self, aging_threshold):
        super().__init__(aging_threshold)
        
  def sort_jobs_by_arrival_time(self, jobs):
    # Sort jobs by their execution time (third variable)
    jobs = sorted(jobs, key=lambda job: job.arrival_time)
    sorted_jobs = jobs
    return sorted_jobs

  def process_jobs(self, jobs_to_execute):
      #sort jobs
      jobs_to_execute = self.sort_jobs_by_arrival_time(jobs_to_execute)

      cpu_available = True
      
      #process jobs  
      for i in range(len(jobs_to_execute)):
          if cpu_available:
              # Change the status to running
              jobs_to_execute[i].status = Status.RUNNING
              cpu_available = False
              print(f"-----------------starting JOB {jobs_to_execute[i].job_number}------------------")
              print(f"Job status {jobs_to_execute[i].status.value}")

              # Run the timeline
              chron = Chronometer()
              chron.start()
               
              #executing a job
              while True:
                  current_time = chron.get_current_time()
                  if i + 1 < len(jobs_to_execute) and current_time == jobs_to_execute[i + 1].arrival_time:
                      self.enqueue(jobs_to_execute[i + 1])
                      # print(f"Ready queue : added 1 item")

                  if current_time == jobs_to_execute[i].actual_execution_time:
                      # Changing status of the job after finishing execution
                      jobs_to_execute[i].status = Status.EXIT
                      cpu_available = True
                      print(f"Job status {jobs_to_execute[i].status.value}")
                      print(f"-----------------finishing JOB {jobs_to_execute[i].job_number}------------------")
                      print(f"-----------------Total time elapsed {chron.get_total_time()}------------------")
                      break
      chron.stop()


