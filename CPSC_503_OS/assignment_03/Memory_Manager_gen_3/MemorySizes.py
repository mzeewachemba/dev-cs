import re


class MemorySizes:
    units = {
        'KB': 1024,
        'MB': 1024 ** 2,
    }

    def __init__(self):
        pass

    def get_memory_size(self, size_str):
        pattern = re.compile(r'(\d+(\.\d+)?)([a-zA-Z]+)')
        match = pattern.match(size_str.strip().upper())
        if not match:
            raise ValueError(f"Invalid memory size format: {size_str}")
        size, _, unit = match.groups()
        size = float(size)
        if unit not in self.units:
            raise ValueError(f"Invalid memory unit: {unit}")
        return size_str, int(size * self.units[unit])

    def get_memory_size_difference(self, size1, size2):
        size1_bytes = self.get_memory_size(size1)[1]
        size2_bytes = self.get_memory_size(size2)[1]
        difference = size1_bytes - size2_bytes
        if abs(difference) < 1024:
            difference_str = f"{difference} bytes"
        elif abs(difference) < 1048576:
            difference_str = f"{difference / 1024:.2f} KB"
        else:
            difference_str = f"{difference / 1048576:.2f} MB"
        size1_str, size1_bytes = self.get_memory_size(size1)
        size2_str, size2_bytes = self.get_memory_size(size2)
        return difference_str, difference

    def compare(self, size1, size2):
        difference = self.get_memory_size_difference(size1, size2)[1]
        if difference < 0:
            return -1
        elif difference > 0 or difference == 0:
            return 1
        else:
            return 0
