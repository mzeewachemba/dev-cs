import re


class MemorySizes:
    units = {
        'KB': 1024,
        'MB': 1024 ** 2,
    }

    def __init__(self):
        pass

    def get_memory_size(self, size_str):
        pattern = re.compile(r'(\d+)([a-zA-Z]+)')
        match = pattern.match(size_str.strip().upper())
        if not match:
            raise ValueError(f"Invalid memory size format: {size_str}")
        size, unit = match.groups()
        size = int(size)
        if unit not in self.units:
            raise ValueError(f"Invalid memory unit: {unit}")
        return size_str, size * self.units[unit]

    def compare(self, size1, size2):
        size1_bytes = self.get_memory_size(size1)
        size2_bytes = self.get_memory_size(size2)
        if size1_bytes < size2_bytes:
            return -1
        elif size1_bytes > size2_bytes:
            return 1
        else:
            return 0
