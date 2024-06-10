from collections import defaultdict


# Function to detect all cycles in a graph
def detect_cycles(graph):
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
def create_graph(dependencies):
    graph = defaultdict(list)
    for start, end in dependencies:
        graph[start].append(end)
    return graph


# Function to process cycles and print them with and without the last number
def process_cycles(cycles):
    cycles_with_last = []
    cycles_without_last = []

    for cycle in cycles:
        # Add cycle with the last number to the list
        cycles_with_last.append(cycle)
        # Create a cycle without the last number and add to the list
        cycle_without_last = cycle[:-1]
        cycles_without_last.append(cycle_without_last)

    # Print cycles with the last number
    print("Cycles with last number:")
    for cycle in cycles_with_last:
        print(" -> ".join(map(str, cycle)))

    # Print cycles without the last number
    print("\nCycles without last number:")
    for cycle in cycles_without_last:
        print(" -> ".join(map(str, cycle)))

    # Check and print cycles without redundancy
    unique_cycles = check_cycles_similarity(cycles_without_last)
    print("\nCycles after applying redundancy:")
    for cycle in unique_cycles:
        print(" -> ".join(map(str, cycle)))


# Function to check if all cycles without the last number are the same
def check_cycles_similarity(cycles):
    if not cycles:
        return []

    # Normalize the cycles for comparison
    normalized_cycles = [normalize_cycle(cycle) for cycle in cycles]

    # Check if all normalized cycles are the same
    first_cycle = normalized_cycles[0]
    all_same = all(cycle == first_cycle for cycle in normalized_cycles)

    if all_same:
        return [first_cycle]
    else:
        return cycles


# Function to normalize a cycle (to handle rotations)
def normalize_cycle(cycle):
    if not cycle:
        return cycle
    min_index = cycle.index(min(cycle))
    return cycle[min_index:] + cycle[:min_index]


def main():
    # dependencies = [(1, 2), (2, 3), (3, 1)]
    # dependencies = [(1, 4), (4, 2), (1, 2), (2, 3), (3, 1)]
    dependencies = [(1, 2), (2, 3), (3, 4), (4, 1),]

    graph = create_graph(dependencies)
    cycles = detect_cycles(graph)

    process_cycles(cycles)


if __name__ == "__main__":
    main()
