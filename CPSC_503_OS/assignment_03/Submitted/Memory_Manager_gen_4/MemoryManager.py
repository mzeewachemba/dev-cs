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
        self.total_fragments_memory = 0

        # 19 partition sizes that sum to 32MB
        partition_sizes = [
            "128KB",
            "128KB",
            "4MB",
            "2MB",
            "8MB",
            "256KB",
            "7MB",
            "2MB",
            "1MB",
            "512KB",
            "1MB",
            "512KB",
            "256KB",
            "128KB",
            "1MB",
            "1MB",
            "1MB",
            "1MB",
            "128KB"
        ]

        # Create and add partitions and alternatively set them as unavailable and available
        is_available = True
        for size in partition_sizes:
            partition_size = MS.get_memory_size(size)
            partition = Partition(partition_size)
            partition.is_available = is_available
            self.partitions.append(partition)
            is_available = not is_available

    def check_memory(self, job):
        if self.fitting_algorithm == FittingAlgorithm.FIRST_FIT:
            self.first_fit(job)

    def first_fit(self, job):
        MS = MemorySizes()
        for i, partition in enumerate(self.partitions):
            difference = MS.get_memory_size_difference(partition.partition_size[0], job.memory_size[0])
            if partition.is_available and MS.compare(partition.partition_size[0],
                                                     job.memory_size[0]) == 1:  # getting first available partition
                print(f"Difference is {difference}")
                partition.is_available = False
                partition.process_id = job.job_number
                partition.partition_size = job.memory_size

                # Add new partition with the size of the difference right after the current partition
                if difference[1] > 0:
                    new_partition = Partition(partition_size=difference)
                    self.partitions.insert(i + 1, new_partition)
                    self.total_fragments_memory += difference[1]

                return True
        return False

    def release_memory(self, job_number):
        for partition in self.partitions:
            if partition.process_id == job_number:
                partition.is_available = True
                partition.process_id = None

    def get_partitions(self):
        print(f">>>>>>>>>>>>>>>We have {len(self.partitions)} Partitions and their status: ")

        for partition in self.partitions:
            print(
                f"Size {partition.partition_size},process id {partition.process_id} , "
                f"availability {partition.is_available}")

    # Fragmentation Percentage = (Σ Size of free blocks added) / Total  free memory * 100
    # how many fragments we are adding on top of free memory
    def calculate_fragmentation_percentage(self):
        free_memory = sum(partition.partition_size[1] for partition in self.partitions if partition.is_available)

        fragmentation_percentage = (self.total_fragments_memory / free_memory) * 100

        # print totaml free memory and total fragmentation memory
        # print(f"Total free memory: {free_memory} bytes")
        # print(f"Total fragmentation memory: {self.total_fragments_memory} bytes")
        return fragmentation_percentage
