from NQueensProblem import NQueensProblem
from csp_helper_functions import minimum_remaining_values

# Author: Ben Williams '25
# Date: October 15th, 2023

# num_queens = 4
# num_queens = 8
# num_queens = 16
# num_queens = 24
num_queens = 64

# Eight queens
queens_problem = NQueensProblem(num_queens)

# print(f'Testing backtracking with heuristics on {num_queens} queens:')
# solution = queens_problem.backtracking_solver(inference=queens_problem.MAC3, select_variable=minimum_remaining_values,
#                                               order_domain=queens_problem.least_constraining_value)
# queens_problem.illustrate_solution(solution)
# print(queens_problem.get_and_reset_search_calls(), "Total search calls")
# print("----------------\n")

print(f'Testing min-conflicts on {num_queens} queens:')
solution, iterations = queens_problem.local_search(10000)
queens_problem.illustrate_solution(solution)
print(iterations, "Total iterations")
print("----------------\n")

print("Testing how often min-conflicts fails:")
fails = 0
total_iters = 0
for i in range(100):
    solution, iterations = queens_problem.local_search(10000)
    if not solution:
        fails += 1
    else:
        total_iters += iterations
print(f'Failure frequency: {fails}%, average iterations for success: {total_iters / (100 - fails)}')