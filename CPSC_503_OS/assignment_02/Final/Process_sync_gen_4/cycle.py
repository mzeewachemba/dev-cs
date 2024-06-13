import random
from collections import defaultdict


class Cycle:
    def __init__(self):
        pass

    # Create a graph from the given dependencies
    def create_graph(self, dependencies):
        graph = defaultdict(list) # dictionary where each key points to a list of nodes it has edges to
        for start, end in dependencies:
            graph[start].append(end)
        return graph

    # Function to detect all cycles in a graph
    def detect_cycles(self, graph): #depth first search to traverse the graph to determine different paths for a cycle recursively
        def dfs(node, start, visited, stack, path):
            visited.add(node)
            stack.add(node)
            path.append(node)

            # iterates over each neighbor of the current node
            for neighbor in graph[node]:
                if neighbor not in visited: # if the neighbor has not been visited call dfs on it
                    if dfs(neighbor, start, visited, stack, path):
                        return True
                elif neighbor in stack and neighbor == start: # if the neighbor is a start node and is in the stack
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
        print(f"\nUnique Cycles without redundancy is : {unique_cycles}")
        print("\nNon redundant Cycles:")
        for cycle in unique_cycles:
            print(" -> ".join(map(str, cycle)))
        return unique_cycles

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
    # returns the reordered cycle, normalized to start from the smallest element
    def normalize_cycle(self, cycle):
        if not cycle:
            return cycle
        min_index = cycle.index(min(cycle))
        return cycle[min_index:] + cycle[:min_index]

    # Function to break the unique cycle by determining all processes dependent on each other(no of pre emptions)
    # and select one and pull out the resource causing dependency
    def break_cycle(self, cycles, processes_with_dependencies):
        print(f"\nBreaking Cycles:")
        #Determining no of pre emptions
        preemption_list = []
        for cycle in cycles:
            for process in cycle:
                process_obj = processes_with_dependencies[process - 1]
                if process_obj.process_no in cycle:
                    dependency_tuple = (
                        process_obj.process_no,
                        process_obj.dependency_relationship.process_no,
                        process_obj.dependency_relationship.alloted_resource
                    )
                    preemption_list.append(dependency_tuple)
                    # print(f"Process {process_obj.process_no} depends on {process_obj.dependency_relationship.process_no} "
                    #       f"for resource {process_obj.dependency_relationship.alloted_resource}")
        print(f"Processes for pre-emptions: { preemption_list}")

        #Randomly selecting one process for pre-emption and remove its alloted resource
        selected_entry = random.choice(preemption_list)
        for process in processes_with_dependencies:
            if process.process_no == selected_entry[0]:
                process.alloted_resource = None #removing alloted resource

        #printing processes_with_dependencies with one alloted resource removed to avoid deadlock
        print(f"\nProcesss with dependencies after removing resource")
        for process in processes_with_dependencies:
            print(f"Process {process.process_no} has alloted resource {process.alloted_resource}")


        print(f"Selected process for pre-emption: {selected_entry[0]}")
        return preemption_list


