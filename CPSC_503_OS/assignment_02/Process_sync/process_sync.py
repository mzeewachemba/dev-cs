class process():
    def __init__(self , process_no , alloted_resource , requested_resource):
        self.process_no = process_no
        self.alloted_resource = alloted_resource
        self.requested_resource = requested_resource

class reduction():
    def parse_process_resource_allocation_graph(self , file):
        process_and_resources = []
        with open(file, 'r') as file:
            for line in file:
                # Remove trailing newline character
                line = line.strip()
                # Split the line into words using whitespace as delimiter
                num = line.split()
                process_and_resources.append(num)
        return process_and_resources



def main():
    file = ".\process_resource_allocation_graph.txt"

    red = reduction()
    process_and_resources_parsed = red.parse_process_resource_allocation_graph(file)

    # for line_num, nums in enumerate(process_and_resources_parsed):
    #     print(f"Line {line_num + 1}: {nums}")

if __name__ == "__main__":
    main()

