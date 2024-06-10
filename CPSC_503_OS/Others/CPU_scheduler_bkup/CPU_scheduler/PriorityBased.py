from LinearQueue import LinearQueue

class PriorityBased(LinearQueue):
  """
  This class represents a priority-based queue.
  """
  def __init__(self, aging_threshold , switch):
    super().__init__(aging_threshold)
    self.switch = switch
