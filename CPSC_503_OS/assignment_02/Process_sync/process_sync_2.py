class Process:
    def __init__(self, process_no, alloted_resource, requested_resource):
        self.process_no = process_no
        self.alloted_resource = alloted_resource
        self.requested_resource = requested_resource
        self.dependency_relationship = None

    def __str__(self):
        dependency_str = f"Process {self.dependency_relationship.process_no}" if self.dependency_relationship else "None"
        return (f"Process {self.process_no} - Allotted: {self.alloted_resource}, Requested: {self.requested_resource} , "
                f"Dependency relationship: {dependency_str}")


class Reduction:
    def parse_process_resource_allocation_graph(self, file):
        processes = []
        with open(file, 'r') as file:
            for line in file:
                # Remove trailing newline character
                line = line.strip()
                # Split the line into words using whitespace as delimiter
                num = line.split()
                if len(num) == 3:
                    process_no = int(num[0])
                    alloted_resource = int(num[1])
                    requested_resource = int(num[2])
                    proc = Process(process_no, alloted_resource, requested_resource)
                    processes.append(proc)
        return processes

    def establish_dependencies(self, processes):
        n = len(processes)
        dependency_matrix = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i != j:
                    if processes[i].requested_resource == processes[j].alloted_resource:
                        dependency_matrix[i][j] = 1
                        processes[i].dependency_relationship = processes[j]

        return dependency_matrix, processes

    def print_dependency_matrix(self, processes, dependency_matrix):
        process_numbers = [p.process_no for p in processes]

        # Print the header
        print("\nDependency Matrix:")
        print("    ", " ".join(f"P{num}" for num in process_numbers))

        # Print each row with row headers
        for i, row in enumerate(dependency_matrix):
            print(f"P{process_numbers[i]:<3}", " ".join(map(str, row)))


def main():
    file = "./process_resource_allocation_graph.txt"

    red = Reduction()
    processes = red.parse_process_resource_allocation_graph(file)

    for proc in processes:
        print(proc)

    dependency_matrix, processes_with_dependencies = red.establish_dependencies(processes)
    red.print_dependency_matrix(processes, dependency_matrix)

    for proc in processes_with_dependencies:
        print(proc)


if __name__ == "__main__":
    main()
