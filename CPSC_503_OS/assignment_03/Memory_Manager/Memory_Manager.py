from enum import Enum
from Memory_Sizes import MemorySizes


class FittingAlgorithm(Enum):
    FIRST_FIT = 1
    BEST_FIT = 2
    WORST_FIT = 3

class Partition:
    def __init__(self , size):
        self.process_id = None
        self.partition_size = 0
        self.is_available = True

class MemoryManager:
    def __init__(self, fitting_algorithm):
        MS = MemorySizes()
        self.main_memory_size = MS.get_memory_size("32MB")
        self.fitting_algorithm = fitting_algorithm
        self.partitions = [] # contains partitions

    def allocate_job(self, job):
        pass
