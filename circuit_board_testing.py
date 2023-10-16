from CircuitBoardProblem import CircuitBoardProblem
from datetime import datetime
from csp_helper_functions import minimum_remaining_values

# Author: Ben Williams
# Date: October 10th, 2023

# #####################################
# The given example / the smallest test
# #####################################
# test_components_small = [(3, 2), (5, 2), (2, 3), (7, 1)]
# test_cbp = CircuitBoardProblem(10, 3, test_components_small)

# #####################################
# A medium test that even basic backtracking can finish
# #####################################
test_components_medium = [(5, 5), (3, 3), (2, 2), (1, 4), (4, 1), (2, 2), (1, 4), (4, 1), (6, 1), (4, 2)]
test_cbp = CircuitBoardProblem(15, 5, test_components_medium)

# #####################################
# A hard test that we need to use all the heuristics to finish
# 4x the small test with an additional 2x2 component
# #####################################
# test_components_big = [(3, 2), (5, 2), (2, 3), (7, 1), (3, 2), (5, 2), (2, 3), (7, 1), (3, 2), (5, 2), (2, 3), (7, 1), (3, 2), (5, 2), (2, 3), (7, 1), (2, 2)]
# test_cbp = CircuitBoardProblem(20, 6, test_components_big)

# print("Testing brute force solver")
# solution_bf = test_cbp.brute_force_solver()
# test_cbp.illustrate_solution(solution_bf)
# print(test_cbp.get_and_reset_search_calls(), "total search calls")
start = datetime.now()
print("Testing backtracking")
solution_no_inference = test_cbp.backtracking_solver()
test_cbp.illustrate_solution(solution_no_inference)
print(test_cbp.get_and_reset_search_calls(), "total search calls")
end = datetime.now()
print("Time elapsed:", end - start)
print("----------------\n")


# print(test_cbp.constraints[(0, 1)])
# flipped_1_0 = set()
# for pair in test_cbp.constraints[(1, 0)]:
#     flipped_1_0.add((pair[1], pair[0]))
# print(test_cbp.constraints[(0, 1)] == flipped_1_0)

print("Testing backtracking with inference")
solution_with_inference = test_cbp.backtracking_solver(inference=test_cbp.MAC3)
test_cbp.illustrate_solution(solution_with_inference)
print(test_cbp.get_and_reset_search_calls(), "total search calls")
print("----------------\n")

print("Testing backtracking with inference and min-remaining-values")
solution_i_mrv = test_cbp.backtracking_solver(inference=test_cbp.MAC3, select_variable=minimum_remaining_values)
test_cbp.illustrate_solution(solution_i_mrv)
print(test_cbp.get_and_reset_search_calls(), "total search calls")
print("----------------\n")

print("Testing backtracking with inference and least-constraining-value")
solution_i_lcv = test_cbp.backtracking_solver(inference=test_cbp.MAC3, select_variable=minimum_remaining_values)
test_cbp.illustrate_solution(solution_i_lcv)
print(test_cbp.get_and_reset_search_calls(), "total search calls")
print("----------------\n")

print("Testing backtracking with inference, min-remaining-values, and least-constraining-value")
solution_i_lcv_mrv = test_cbp.backtracking_solver(inference=test_cbp.MAC3, select_variable=minimum_remaining_values,
                                                   order_domain=test_cbp.least_constraining_value)
test_cbp.illustrate_solution(solution_i_lcv_mrv)
print(test_cbp.get_and_reset_search_calls(), "total search calls")
print("----------------\n")

print("Testing local search")
start = datetime.now()
solution_ls, iterations = test_cbp.local_search(100000)
print("Num-iterations", iterations)
test_cbp.illustrate_solution(solution_ls)
end = datetime.now()
print("Time elapsed:", end - start)








