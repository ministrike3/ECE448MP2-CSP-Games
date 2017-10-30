import random
from CSPsmart import *
# Functions that exist in CSP smart
#can_color_be_assigned_here
#get_four_neighbors
#get_four_neighbors_colors

def forward_checking(solve_dict,color_set,initial_points,height,width):
    def forward_color_check(solve_dict, color_set, initial_points, square, height, width):
        for color in color_set:
            if can_color_be_assigned_here(color, square, solve_dict, height, width, initial_points) == True:
                return True
        return False

    list_of_total_keys=[]
    for row in range(0,height):
        for col in range(0,width):
            if (row,col) not in solve_dict.keys():
                list_of_total_keys.append((row,col))

    for i in list_of_total_keys:
        if forward_color_check(solve_dict, color_set, initial_points, i, height, width)==False:
            return(False)
    return(True)

def get_next_variable_to_assign(solution_set,height,width,color_list,initial_points):
    #returns a 2-D tuple of (row, column) that DOES NOT already exist in the solution set
    row_array=[]
    for i in range(0,height):
        row_array.append(i)
    random.shuffle(row_array)

    min_of_colors=len(color_list)
    said_spots_number_of_neighbors=0

    col_array=[]
    which_to_return=None
    for i in range(0,width):
        col_array.append(i)
    random.shuffle(col_array)
    for row in row_array:
        for column in col_array:
            if (row, column) not in solution_set:
                count=0
                neighbors=get_four_neighbors((row, column),height,width)
                for i in neighbors:
                    if i != None:
                        if i in solution_set.keys():
                            count+=1

                number_of_colors = 0
                for color in color_list:
                    #can_color_be_assigned_here(color, coordinates, solve_dict,height,width,initial_points):
                    coords=(row, column)
                    if can_color_be_assigned_here(color, coords, solution_set, height, width, initial_points):
                        number_of_colors+=1

                if number_of_colors==min_of_colors:

                    if count>said_spots_number_of_neighbors:
                        said_spots_number_of_neighbors=count
                        which_to_return=(row, column)

                if number_of_colors < min_of_colors:
                    said_spots_number_of_neighbors = count
                    which_to_return = (row, column)

    yield (which_to_return)

    # for row in range(height):
    #     for column in range(width):
    #         if (row, column) not in solution_set.keys():
    #             yield (row, column)
def torder_of_colors():
    pass