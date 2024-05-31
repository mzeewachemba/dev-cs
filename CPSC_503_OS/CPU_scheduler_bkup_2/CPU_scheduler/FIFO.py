from Chronometer import Chronometer
from Status import Status
from LinearQueue import LinearQueue

class FIFO(LinearQueue):
  """
  This class represents a linear queue with an aging threshold.
  """
  def __init__(self, aging_threshold):
      super().__init__(aging_threshold)

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
