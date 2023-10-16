from ConstraintSatisfactionProblem import ConstraintSatisfactionProblem

# Author: Ben Williams '25
# Date: October 15th, 2023


class NQueensProblem(ConstraintSatisfactionProblem):
    def __init__(self, num_queens):
        self.variables = [i for i in range(num_queens)]
        # Define the domains by giving each queen a column
        # This makes constraints simpler, as we only need to worry about the horizontal and diagonal
        self.domains = [[j * num_queens + i for j in range(num_queens)] for i in range(num_queens)]

        # Not necessary since we can use len(self.variables), but makes for more readable code
        self.board_width = num_queens
        self.board_height = num_queens

        self.constraints = dict()
        # Really just looping through all the queens
        for var in range(len(self.variables)):
            self.add_queen_constraints(var)

        super().__init__(self.variables, self.domains, self.constraints)

    # Add all the constraints for one queen
    def add_queen_constraints(self, var):
        column = self.domains[var][0]
        for location in self.domains[var]:
            defending_locations = set()

            # Add all horizontal spaces that the queen defends
            for horizontal in range(self.board_width):
                defending_locations.add(location + horizontal - column)

            # Add all the diagonals
            defending_locations = defending_locations.union(self.get_diagonals_threatened(location))

            # Loop through all locations on the board, and add relevant constraints
            for other_loc in range(self.board_width * self.board_height):
                relevant_queen = other_loc % self.board_width
                if relevant_queen == var:
                    continue

                if other_loc not in defending_locations:
                    if (var, relevant_queen) not in self.constraints.keys():
                        self.constraints[(var, relevant_queen)] = set()
                    self.constraints[(var, relevant_queen)].add((location, other_loc))

    # Given a location, return a set of all the diagonal spaces that would be threatened by a queen
    def get_diagonals_threatened(self, location):
        column = location % self.board_width
        diagonals = set()

        col_pos = self.board_height - column
        col_neg = column
        # How many rows are below us, or positive as far as the index goes
        for row_pos in range(self.board_height - location // self.board_width):
            if row_pos == 0:
                continue

            # We are looking farther down than necessary
            if row_pos > col_pos and row_pos > col_neg:
                break

            # Add bottom-right
            if row_pos <= col_pos:
                diagonal = location + row_pos + (row_pos * self.board_width)
                diagonals.add(diagonal)

            # Add bottom-left
            if row_pos <= col_neg:
                diagonal = location - row_pos + (row_pos * self.board_width)
                diagonals.add(diagonal)

        # How many rows are above us, or negative as the index goes
        for row_neg in range(location // self.board_width + 1):
            if row_neg == 0:
                continue

            # We are looking farther up than necessary
            if row_neg > col_pos and row_neg > col_neg:
                break

            # Add top-right
            if row_neg <= col_pos:
                diagonal = location + row_neg - (row_neg * self.board_width)
                diagonals.add(diagonal)

            # Add top-left
            if row_neg <= col_neg:
                diagonal = location - row_neg - (row_neg * self.board_width)
                diagonals.add(diagonal)

        return diagonals

    # Illustrate an assignment with the queens on the board
    def illustrate_solution(self, assignment):
        if assignment is None:
            print("No Solution")
            return

        set_assignment = set(assignment)
        for col in range(self.board_width):
            row_str = ""
            for row in range(self.board_height):
                # Order of queens does not matter
                if row + (col * self.board_width) not in set_assignment:
                    # The space makes it easier to actually see the solution
                    row_str += ". "
                else:
                    row_str += "Q "
            print(row_str)


if __name__ == "__main__":
    four_qp = NQueensProblem(4)
    print(four_qp.domains[0])
    print(four_qp.constraints[(0, 1)])
    solution = four_qp.backtracking_solver()
    print(solution)
    four_qp.illustrate_solution(solution)




