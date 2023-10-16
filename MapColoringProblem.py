from ConstraintSatisfactionProblem import ConstraintSatisfactionProblem
from map_coloring_helper_functions import *
# Author: Ben Williams '25
# Date: October 8th, 2023


# An implementation of the k-coloring map problem as an inheritance of a
#   constraint satisfaction problem
class MapColoringProblem(ConstraintSatisfactionProblem):
    def __init__(self, map_file, num_colors):
        # Get the variables, their neighbors, and the references for the names
        variables, neighbors = parse_map_file(map_file)

        # All places on the map have the same domain
        domain = [[i for i in range(num_colors)] for j in range(len(variables))]

        # Build the constraints
        constraints = dict()
        for variable in variables:
            for neighbor in neighbors[variable]:
                constraints[(variable, neighbor)] = set()
                all_pair_tuples(constraints[variable, neighbor], domain[variable])

        super().__init__(variables, domain, constraints)



