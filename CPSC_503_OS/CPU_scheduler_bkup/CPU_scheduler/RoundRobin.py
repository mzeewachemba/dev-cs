from LinearQueue import LinearQueue

class RoundRobin(LinearQueue):
  """
  This class represents a round-robin queue with a time slot.
  """
  def __init__(self, aging_threshold, time_slot ,switch):
    super().__init__(aging_threshold)
    self.time_slot = time_slot
    self.switch = switch
