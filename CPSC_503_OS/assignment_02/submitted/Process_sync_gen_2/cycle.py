from collections import defaultdict

class Cycle:
    def __init__(self):
        pass

    # Function to detect all cycles in a graph
    def detect_cycles(self, graph):
        def dfs(node, start, visited, stack, path):
            visited.add(node)
            stack.add(node)
            path.append(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor, start, visited, stack, path):
                        return True
                elif neighbor in stack and neighbor == start:
                    path.append(neighbor)
                    cycles.append(path[:])
                    path.pop()

            stack.remove(node)
            path.pop()
            return False

        cycles = []
        for node in graph:
            visited = set()
            stack = set()
            path = []
            dfs(node, node, visited, stack, path)

        return cycles

    # Create a graph from the given dependencies
    def create_graph(self, dependencies):
        graph = defaultdict(list)
        for start, end in dependencies:
            graph[start].append(end)
        return graph

    # Function to process cycles and print them with and without the last number
    def process_cycles(self, cycles):
        cycles_with_last = []
        cycles_without_last = []

        for cycle in cycles:
            # Add cycle with the last number to the list
            cycles_with_last.append(cycle)
            # Create a cycle without the last number and add to the list
            cycle_without_last = cycle[:-1]
            cycles_without_last.append(cycle_without_last)

        # Print cycles with the last number
        print("\nCycles with last number:")
        for cycle in cycles_with_last:
            print(" -> ".join(map(str, cycle)))

        # Print cycles without the last number
        print("\nCycles without last number:")
        for cycle in cycles_without_last:
            print(" -> ".join(map(str, cycle)))

        # Check and print cycles without redundancy
        unique_cycles = self.check_cycles_similarity(cycles_without_last)
        print("\nNon redundant Cycles:")
        for cycle in unique_cycles:
            print(" -> ".join(map(str, cycle)))

    # Function to check if all cycles without the last number are the same
    def check_cycles_similarity(self, cycles):
        if not cycles:
            return []

        # Normalize the cycles for comparison
        normalized_cycles = [self.normalize_cycle(cycle) for cycle in cycles]

        # Check if all normalized cycles are the same
        first_cycle = normalized_cycles[0]
        all_same = all(cycle == first_cycle for cycle in normalized_cycles)

        if all_same:
            return [first_cycle]
        else:
            return cycles

    # Function to normalize a cycle (to handle rotations)
    def normalize_cycle(self, cycle):
        if not cycle:
            return cycle
        min_index = cycle.index(min(cycle))
        return cycle[min_index:] + cycle[:min_index]