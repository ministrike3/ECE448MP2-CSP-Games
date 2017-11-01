# In This file only write the main function. Define functions in either readInput or CSPSolving
from readInput import *
from CSPsmart import *
from heuristics import *
import time
import random


def smart_solver(solve_dict,height,width,color_set,initial_points):
    global assignments
    color_list=list(color_set)
    random.shuffle(color_list)

    if len(solve_dict)==height*width:
        return solve_dict

    getnext=get_next_variable_to_assign(solve_dict,height,width,color_list,initial_points)


    for current_coordinates in getnext:
        colorz=order_of_colors(solve_dict,color_list, current_coordinates,height,width,initial_points)
        for color in colorz:
            if can_color_be_assigned_here(color, current_coordinates, solve_dict,height,width,initial_points):
                assignments+=1
                #print("Put " + color + " IN " + str(current_coordinates))
                solve_dict[current_coordinates] = color
                if assignments%100==0:
                    print_free_flow(solve_dict, height, width)
                    print('\n')
                    pass

                if forward_checking(solve_dict, color_set, initial_points, height, width):
                    recursive_call = smart_solver(solve_dict,height,width,color_set,initial_points)
                    if recursive_call != None:
                        return (recursive_call)
                #print('Had to Pop '+color+' From '+str(current_coordinates))
                solve_dict.pop(current_coordinates)
        return (None)

if __name__ == "__main__":
    games = get_list_of_test_files()
    #for gameboard in games:
    gameboard=games[0]
    name = get_name(gameboard)
    useful_array_board = input_to_array(gameboard)
    height, width = puzzleDetails(useful_array_board)
    print("height:", height, "width:", width)
    for row in useful_array_board:
        print(row)

    print('\n')

    color_set, solve_dict = generateColorSet_Dict(useful_array_board)

    #print("colorSet:", color_set, "colorDict:", solve_dict)
    initial_points = solve_dict.copy()
    #THESE COMMENTS ARE IMPORTANT EVENTUALLY WE'RE SUPPOSED TO HAVE AVERAGES so I figured 10 is good
    average_time=0
    average_assignments=0
    for i in range(0,10):
        solved_maze_input=solve_dict.copy()
        start=time.time()
        assignments=0
        solved_maze=smart_solver(solved_maze_input,height,width,color_set,initial_points)
        end=time.time()
        average_time += (end-start)
        average_assignments +=assignments
        print((average_assignments/(i+1),average_time/(i+1)))
    average_assignments=average_assignments/i
    average_time=average_time/i

    print('\n')
    #print(end-start)
    #print(assignments)
    print(average_time)
    print(average_assignments)
    #print(solved_maze)
    print('\n')
    print_free_flow(solved_maze,height,width)
    filename = 'Outputs/%s.txt' % name
    print_free_flow_file(solved_maze, height, width,str(end-start),str(assignments),filename)
    print('______________________________________________')
