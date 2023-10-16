# Author: Ben Williams '25
# Date: October 8th, 2023

# Goes through a map file and returns a list of states and neighbors
#   in the format of a CSP
# Parameter: file_name - String of the location of the map file
def parse_map_file(file_name):
    f = open(file_name, "r")
    variables = []
    neighbors = []
    name_index_map = dict()

    # Read file line by line and parse the map info until we reach the end
    line = f.readline()
    while line:
        line = line.strip()
        node_and_neighbors = line.split("; ")

        # Isolated node - Need to adjust string to remove ";"
        if len(node_and_neighbors) == 1:
            node_and_neighbors[0] = node_and_neighbors[0].strip(";")

        # Check if we have seen this node as a neighbor of another node
        if node_and_neighbors[0] not in name_index_map.keys():
            # We will refer to this province as an integer
            variables.append(len(variables))
            # Need to subtract 1 to adjust for the longer list after appending
            name_index_map[node_and_neighbors[0]] = len(variables) - 1
            neighbors.append([])

        # Isolated node - we are finished here
        if len(node_and_neighbors) == 1:
            line = f.readline()
            continue

        # Loop through and handle all the neighbors
        neighbor_variables = node_and_neighbors[1].split(", ")
        for neighbor in neighbor_variables:
            # If we haven't seen this variable before
            if neighbor not in name_index_map.keys():
                variables.append(len(variables))
                name_index_map[neighbor] = len(variables) - 1
                neighbors.append([])

            # Add this neighbor to the list of neighbors for the variable's index
            neighbors[name_index_map[node_and_neighbors[0]]].append(name_index_map[neighbor])

        # Continue onto the next line
        line = f.readline()

    f.close()
    return variables, neighbors


# Takes the domain and adds all possible non-overlapping pairs into the list
# Meant to represent non-bordering colors. If the domain is {0, 1},
#   then (0, 1) and (1, 0) will be added, but not (0, 0).
def all_pair_tuples(given_set, domain):
    for i in domain:
        for j in domain:
            if i != j:
                given_set.add((i, j))



