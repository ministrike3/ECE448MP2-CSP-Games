# In This file only write the main function. Define functions in either readInput or CSPSolving
from readInput import *
from CSPSolving import *



def dumb_solver(solve_dict,height,width,color_set):
    # Thoughts

    # For every empty square, form a set of possible colours for that square, and then repeatedly perform
    # logical deductions at each square to shrink the allowed set of colours for that square.

    # Whenever a square's set of possible colours shrinks to size 1, the colour for that square is determined.

    # If there are no more squares with logical deductions to perform and the puzzle is not completely solved yet
    # because some squares have more than one possibilty left,  pick one of these undecided squares
    # and recurse on it, trying each of the possible colours in turn.

    # Each try will either lead to a solution, or a contradiction.
    # If contradiction eliminate that colour as a possibility for that square.

    # When picking a square to branch on, it's generally a good idea to pick a square with
    # as few allowed colours as possible.


    for current_coordinates in get_next_variable_to_assign(solve_dict,height,width):
        for color in color_set:
            print("Attempting to Put " + color + " IN " + str(current_coordinates))
            if can_color_be_assigned_here(color, current_coordinates, solve_dict):
                solve_dict[current_coordinates] = color
                recursive_call = dumb_solver(solve_dict, color_set)
                if recursive_call != None:
                    return recursive_call
                solve_dict.pop(current_coordinates)
    return None


