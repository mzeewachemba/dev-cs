class LinearQueue:
  """
  This class represents a linear queue with an aging threshold.
  """
  def __init__(self, aging_threshold):
    self.aging_threshold = aging_threshold
    self.ready_queue = []
    
  def is_empty(self):
    """
    Checks if the queue is empty.
    """
    return len(self.ready_queue) == 0

  def enqueue(self, job):
    """
    Adds a job to the end of the queue.
    """
    self.ready_queue.append(job)
    self.ready_queue = self.deduplicate(self.ready_queue)


  def dequeue(self):
    """
    handles aging
    """
    # if self.is_empty():
    #   return None

    # # Check for jobs exceeding the aging threshold
    # aged_jobs = [job for job in self.queue if job.arrival_time + self.aging_threshold < time.time()]
    # if aged_jobs:
    #   # Remove aged jobs
    #   for job in aged_jobs:
    #     self.ready_queue.remove(job)

    # return self.ready_queue.pop(0)

  def deduplicate(self, jobs):
      seen = set()
      deduplicated_jobs = []
      for job in jobs:
          if job not in seen:
              seen.add(job)
              deduplicated_jobs.append(job)
      return deduplicated_jobs