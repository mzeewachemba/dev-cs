from LinearQueue import LinearQueue

class ShortJobFirst_SJF(LinearQueue):
  """
  This class represents a priority-based queue.
  """
  def __init__(self, aging_threshold , switch):
    super().__init__(aging_threshold)
