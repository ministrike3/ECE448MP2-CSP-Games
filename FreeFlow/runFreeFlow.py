# In This file only write the main function. Define functions in either readInput or CSPSolving
from readInput import *
from CSPSolving import *



def dumb_solver(solve_dict,height,width,color_set,initial_points):
    if len(solve_dict)==25:
        return solve_dict
    getnext=get_next_variable_to_assign(solve_dict,height,width)
    for current_coordinates in getnext:
        for color in color_set:
            if can_color_be_assigned_here(color, current_coordinates, solve_dict,height,width,initial_points):
                print("Put " + color + " IN " + str(current_coordinates))
                solve_dict[current_coordinates] = color
                print_free_flow(solve_dict, height, width)
                recursive_call = dumb_solver(solve_dict,height,width,color_set,initial_points)
                if recursive_call != None:
                    return recursive_call
                print('Had to Pop '+color+' From '+str(current_coordinates))
                solve_dict.pop(current_coordinates)
    return None


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
#It's important to avoid the possibility of forming invalid "loops" of pipe.
# One way to do this is by maintaining, for each allowed colour i of each square x, 2 bits of information:
# whether the square x is connected by a path of definite i-coloured tiles to the first i-coloured endpoint,
# and the same thing for the second i-coloured endpoint.

# Then when recursing, don't ever pick a square that has two neighbours with the
# same bit set (or with neither bit set) for any allowed colour.]


if __name__ == "__main__":
    games = get_list_of_test_files()
    for gameboard in games:
        name = get_name(gameboard)
        useful_array_board = input_to_array(gameboard)
        for row in useful_array_board:
            print(row)
        print('\n')
        height, width = puzzleDetails(useful_array_board)
        print("height:", height, "width:", width)
        color_set, solve_dict = generateColorSet_Dict(useful_array_board)
        print("colorSet:", color_set, "colorDict:", solve_dict)
        initial_points = solve_dict.copy()
        solved_maze=dumb_solver(solve_dict,height,width,color_set,initial_points)
        print('\n')
        print_free_flow(solved_maze,height,width)