class Job:
  """
  This class represents a job in a queueing system.
  """
  def __init__(self, job_number, arrival_time, actual_execution_time, priority, queue_number , status):
    self.job_number = job_number
    self.arrival_time = arrival_time
    self.actual_execution_time = actual_execution_time
    self.priority = priority
    self.queue_number = queue_number
    self.status = status
    
  def __iter__(self):
    """
    Defines an iterator that yields the job's attributes in a specific order.
    """
    attributes = [self.job_number, self.arrival_time, self.actual_execution_time,
                  self.priority, self.queue_number, self.status]
    return iter(attributes)

  def __str__(self):
    """
    Returns a string representation of the Job object.
    """
    return f"Job #{self.job_number} - Arrival: {self.arrival_time:.2f}, Execution Time: {self.actual_execution_time:.2f}, Priority: {self.priority}, Queue: {self.queue_number} ,Status: {self.status}"
