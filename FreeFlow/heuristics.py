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
    said_spots_missing_neighbors=0

    col_array=[]
    which_to_return=None
    for i in range(0,width):
        col_array.append(i)
    random.shuffle(col_array)

    for row in row_array:
        for column in col_array:
            if (row, column) not in solution_set:
                count=0
                not_assigned=0
                neighbors=get_four_neighbors((row, column),height,width)
                for i in neighbors:
                    if i != None:
                        if i in solution_set.keys():
                            count+=1
                        else:
                            not_assigned+=1

                number_of_colors = 0
                for color in color_list:
                    coords=(row, column)
                    if can_color_be_assigned_here(color, coords, solution_set, height, width, initial_points):
                        number_of_colors+=1

                if number_of_colors==min_of_colors:

                    if count>said_spots_number_of_neighbors:
                        said_spots_missing_neighbors = not_assigned
                        said_spots_number_of_neighbors=count
                        which_to_return=(row, column)

                    # if count==said_spots_number_of_neighbors:
                    #     if not_assigned < said_spots_missing_neighbors:
                    #         said_spots_missing_neighbors = not_assigned
                    #         said_spots_number_of_neighbors = count
                    #         which_to_return = (row, column)

                if number_of_colors < min_of_colors:
                    said_spots_missing_neighbors = not_assigned
                    said_spots_number_of_neighbors = count
                    which_to_return = (row, column)

    yield (which_to_return)

    # for row in range(height):
    #     for column in range(width):
    #         if (row, column) not in solution_set.keys():
    #             yield (row, column)

def order_of_colors(solve_dict,color_list,current_coordinates,height,width,initial_points):

    def get_number_of_possibilities(solve_dict,color_list,current_coordinates,height,width,initial_points):
        counter=0
        for row in range(0,height):
            for column in range(0,width):
                if (row, column) not in solve_dict:
                    if (row,column)!=current_coordinates:
                        for color in color_list:
                            if can_color_be_assigned_here(color,(row,column),solve_dict,height,width,initial_points):
                                counter+=1
        return counter

    color_count_array=[0]*len(color_list)

    for i in range(0,len(color_list)):
        solve_dict[current_coordinates]=color_list[i]
        color_count_array[i]=get_number_of_possibilities(solve_dict,color_list,current_coordinates,height,width,initial_points)
        solve_dict.pop(current_coordinates)

    current_max=0
    current_max_index=0
    list_to_return=[]
    #print(color_list)
    #print(color_count_array)

    while len(color_list)>0:
        for i in range(0,len(color_count_array)):
            if color_count_array[i]>current_max:
                current_max = color_count_array[i]
                current_max_index = i
        #if current_max>0:
        list_to_return.append(color_list[current_max_index])
        color_list.pop(current_max_index)
        color_count_array.pop(current_max_index)
        current_max = 0
        current_max_index = 0

    #print('Ret_List')
    #print(list_to_return)
    #print('\n')
    return(list_to_return)
