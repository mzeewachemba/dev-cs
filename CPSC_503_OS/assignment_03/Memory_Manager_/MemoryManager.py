from enum import Enum
from MemorySizes import MemorySizes


class FittingAlgorithm(Enum):
    FIRST_FIT = 1
    BEST_FIT = 2
    WORST_FIT = 3


class Partition:
    def __init__(self, partition_size):
        self.process_id = None
        self.partition_size = partition_size
        self.is_available = True

    def __str__(self):
        return f"Partition(size={self.partition_size} bytes, process_id={self.process_id}, is_available={self.is_available})"

    def get_partition_size(self):
        return self.partition_size


class MemoryManager:
    def __init__(self, fitting_algorithm):
        MS = MemorySizes()
        self.main_memory_size = MS.get_memory_size("32MB")
        self.fitting_algorithm = fitting_algorithm
        self.partitions = []  # contains partitions
        self.fitting_algorithm = fitting_algorithm

        # 15 partition sizes that sum to 32MB
        partition_sizes = [
            "4MB",
            "8MB",
            "2MB",
            "7MB",
            "2MB",
            "1MB",
            "1MB",
            "1MB",
            "512KB",
            "512KB",
            "256KB",
            "256KB",
            "128KB",
            "128KB",
            "128KB"
        ]

        # Create and add partitions
        for size in partition_sizes:
            partition_size = MS.get_memory_size(size)
            partition = Partition(partition_size)
            self.partitions.append(partition)


    def check_memory(self, job):
        if self.fitting_algorithm == FittingAlgorithm.FIRST_FIT:
            self.first_fit(job)

    def first_fit(self, job):
        MS = MemorySizes()
        for partition in self.partitions:
            # print(f"Partition size: {partition.get_partition_size()}")
            # print(f"Job size: {job.memory_size}")
            # print(f"Is partition available: {MS.compare(partition.partition_size[0], job.memory_size[0]) == 1}")
            if partition.is_available and MS.compare(partition.partition_size[0], job.memory_size[0]) == 1: #getting first available partition
                partition.is_available = False
                partition.process_id = job.job_number
                return True
        return False

    def release_memory(self, job_number):
        for partition in self.partitions:
            if partition.process_id == job_number:
                partition.is_available = True
                partition.process_id = None
