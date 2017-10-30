# In This file only write the main function. Define functions in either readInput or CSPSolving
from readInput import *
from CSPdumb import *
import time
import random


def dumb_solver(solve_dict,height,width,color_set,initial_points):
    global assignments
    color_list=list(color_set)
    random.shuffle(color_list)

    if len(solve_dict)==height*width:
        return solve_dict

    getnext=get_next_variable_to_assign(solve_dict,height,width)


    for current_coordinates in getnext:
        for color in color_list:
            if can_color_be_assigned_here(color, current_coordinates, solve_dict,height,width,initial_points):
                assignments+=1
                print("Put " + color + " IN " + str(current_coordinates))
                solve_dict[current_coordinates] = color
                print_free_flow(solve_dict, height, width)
                recursive_call = dumb_solver(solve_dict,height,width,color_set,initial_points)
                if recursive_call != None:
                    return (recursive_call)
                print('Had to Pop '+color+' From '+str(current_coordinates))
                solve_dict.pop(current_coordinates)
        return (None)

if __name__ == "__main__":
    games = get_list_of_test_files()
    for gameboard in games:
        #gameboard=games[-1]
        name = get_name(gameboard)
        useful_array_board = input_to_array(gameboard)
        height, width = puzzleDetails(useful_array_board)
        print("height:", height, "width:", width)
        for row in useful_array_board:
            print(row)

        print('\n')

        color_set, solve_dict = generateColorSet_Dict(useful_array_board)

        print("colorSet:", color_set, "colorDict:", solve_dict)
        initial_points = solve_dict.copy()
        #THESE COMMENTS ARE IMPORTANT EVENTUALLY WE'RE SUPPOSED TO HAVE AVERAGES so I figured 10 is good
        #average_time=0
        #average_assignments=0
        #for i in range(0,10):
        solved_maze_input=solve_dict.copy()
        start=time.time()
        assignments=0
        solved_maze=dumb_solver(solved_maze_input,height,width,color_set,initial_points)
        end=time.time()
        #average_time += (end-start)
        #average_assignments +=assignments
        #average_assignments=average_assignments/10
        #average_time=average_time/10

        print('\n')
        print(end-start)
        print(assignments)
        print(solved_maze)
        print('\n')
        print_free_flow(solved_maze,height,width)
        filename = 'Outputs/%s.txt' % name
        print_free_flow_file(solved_maze, height, width,str(end-start),str(assignments),filename)
        print('______________________________________________')
