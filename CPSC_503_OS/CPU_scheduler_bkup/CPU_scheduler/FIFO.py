from Chronometer import Chronometer
from Status import Status
from LinearQueue import LinearQueue
import time

class FIFO(LinearQueue):
  """
  This class represents a linear queue with an aging threshold.
  """
  def __init__(self, aging_threshold):
    super().__init__(aging_threshold)

  def process_job(self , job_to_execute):
    cpu_available = True

    if cpu_available == True:
      #change the status to running
      job_to_execute.status = Status.RUNNING
      print(f"Job status {job_to_execute.status.value}")
      #run the timeline
      chron = Chronometer()
      chron.run()
      current_time = chron.get_current_time()
      
      if  current_time == job_to_execute.actual_execution_time:
        chron.stop
        # changing status of the job after finishing execution
        job_to_execute.status = Status.EXIT
        print(f"Job status {job_to_execute.status.value}")