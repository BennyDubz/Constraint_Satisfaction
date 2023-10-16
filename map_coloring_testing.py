from MapColoringProblem import MapColoringProblem
from csp_helper_functions import *

# Author: Ben Williams '25
# Date: October 9th, 2023

australia_map_p_3 = MapColoringProblem("./maps/Australia", 3)

print("Variables:", australia_map_p_3.variables)
print("Domains:", australia_map_p_3.domains)
print("Constraints:", australia_map_p_3.constraints)
print("3 Colored Australia solution:")
print(australia_map_p_3.brute_force_solver())
print(australia_map_p_3.get_and_reset_search_calls(), "total brute force search calls")
print("-------------")

australia_map_p_impossible = MapColoringProblem("./maps/Australia", 2)
print("2 Colored Australia solution (should not exist)")
print(australia_map_p_impossible.brute_force_solver())
australia_map_p_3.get_and_reset_search_calls()
print("------")
solution = australia_map_p_3.backtracking_solver()
print(solution)
print(australia_map_p_3.get_and_reset_search_calls(), "Total backtracking search calls")







