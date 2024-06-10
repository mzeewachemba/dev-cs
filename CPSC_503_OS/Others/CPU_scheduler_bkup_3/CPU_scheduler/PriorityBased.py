from LinearQueue import LinearQueue
from Status import Status
from Chronometer import Chronometer


class PriorityBased(LinearQueue):
  """
  This class represents a priority-based queue.
  """
  def __init__(self, aging_threshold , switch):
    super().__init__(aging_threshold)
    self.switch = switch

  def sort_jobs_by_priority(self , jobs):
    # Sort jobs by their execution time (third variable)
    jobs = sorted(jobs, key=lambda job: job.priority, reverse=True)
    sorted_jobs = jobs
    return sorted_jobs

    
  def process_jobs(self, jobs_to_execute):
      cpu_available = True
      
      for job_to_execute in jobs_to_execute: 
          if cpu_available:
              # Change the status to running
              job_to_execute.status = Status.RUNNING
              print(f"-----------------starting JOB {job_to_execute.job_number}------------------")
              print(f"Job status {job_to_execute.status.value}")

              # Run the timeline
              chron = Chronometer()
              chron.start()

              while True:
                  current_time = chron.get_current_time()
                  if current_time == job_to_execute.actual_execution_time:
                      chron.stop()
                      # Changing status of the job after finishing execution
                      job_to_execute.status = Status.EXIT
                      print(f"Job status {job_to_execute.status.value}")
                      print(f"-----------------finishing JOB {job_to_execute.job_number}------------------")
                      break
