from ConstraintSatisfactionProblem import ConstraintSatisfactionProblem

# Author: Ben Williams '25
# Date: October 9th, 2023


# An implementation of the Circuit Board Problem, where we try to place k components
#   with arbitrary widths and heights on a circuit board so that they can all fit
class CircuitBoardProblem(ConstraintSatisfactionProblem):
    def __init__(self, board_width, board_height, components):
        self.board_width = board_width
        self.board_height = board_height
        self.components = components

        # One dimensional array where each index represents a component
        self.variables = []
        self.variable_component_map = dict()
        for component in components:
            self.variable_component_map[len(self.variables)] = component
            self.variables.append(len(self.variables))

        # Get all component domains
        self.domains = [self.get_component_domain(component) for component in components]

        # Get all variable pair constraints
        self.constraints = dict()
        for var_1 in range(len(self.variables)):
            for var_2 in range(len(self.variables)):
                if var_1 != var_2:
                    self.constraints[(var_1, var_2)] = self.get_component_pair_constraints(var_1, var_2)

        # Initialize the parent class with already defined variables, domains, and constraints
        super().__init__(self.variables, self.domains, self.constraints)

    # Find all the places where we can fit the component on the board at all
    # Returns a list of locations (variables) where we can place the top-left corner of the component
    def get_component_domain(self, component):
        domain = []
        # Represents the row

        curr_row = 0
        for location in range(self.board_width * self.board_height):
            if location // self.board_width > curr_row:
                curr_row += 1
            # If we have enough space horizontally
            if location - (curr_row * self.board_width) + component[0] <= self.board_width:
                # If we have enough space vertically
                if component[1] + curr_row <= self.board_height:
                    domain.append(location)

        return domain

    # Given two components, find all pairs of locations where they can be placed
    # Returns a set of tuples of locations
    def get_component_pair_constraints(self, var_1, var_2):
        allowed_pairs = set()

        # Loop through all places we can place the first component
        for curr_location in self.domains[var_1]:
            # A set of locations occupied if the first component is placed at curr_location
            locations_occupied = set()
            for horizontal in range(self.variable_component_map[var_1][0]):
                for vertical in range(self.variable_component_map[var_1][1]):
                    locations_occupied.add(curr_location + horizontal + (vertical * self.board_width))

            # Compare to the places we can place the second component
            #   (Assuming the first component is placed at curr_location)
            for other_location in self.domains[var_2]:
                conflict = False
                for horizontal in range(self.variable_component_map[var_2][0]):
                    for vertical in range(self.variable_component_map[var_2][1]):
                        # If the other component overlaps with the first one, there is a conflict
                        if (other_location + horizontal + (vertical * self.board_width)) in locations_occupied:
                            conflict = True
                            break
                    if conflict:
                        break
                # If there is no conflicts, this is an allowed place for both components
                if not conflict:
                    allowed_pairs.add((curr_location, other_location))

        return allowed_pairs

    # Given a valid assignment, illustrate it in the form of the circuit board problem
    def illustrate_solution(self, assignment):
        if not assignment:
            print("No solution")
            return

        # A dictionary of location --> component
        locations_occupied = dict()

        # Check all components
        for component_var in range(len(assignment)):
            # Allows for illustrating incomplete assignments
            if assignment[component_var] is None:
                continue
            # Loop through all locations that the component occupies
            for horizontal in range(self.variable_component_map[component_var][0]):
                for vertical in range(self.variable_component_map[component_var][1]):
                    location_occupied = assignment[component_var] + horizontal + (vertical * self.board_width)
                    locations_occupied[location_occupied] = chr(ord("A") + component_var)

        # Build the string with . representing empty locations and letters representing individual components
        illustration = ""
        for row in range(self.board_height):
            for col in range(self.board_width):
                if (row * self.board_width) + col not in locations_occupied.keys():
                    illustration += "."
                else:
                    illustration += locations_occupied[(row * self.board_width) + col]
            # Avoid adding the extra new line at the end... personal preference
            if row < self.board_height - 1:
                illustration += "\n"

        print(illustration)


if __name__ == "__main__":
    # Testing domain accuracy
    cbp = CircuitBoardProblem(4, 4, [(2, 2), (2, 2), (2, 3)])
    solution = cbp.brute_force_solver()
    cbp.illustrate_solution(solution)

