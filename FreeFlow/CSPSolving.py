# In This file write all the processing Functions
# (row,column)
import random


def get_next_variable_to_assign(solution_set,height,width):
    #returns a 2-D tuple of (row, column) that DOES NOT already exist in the solution set
    while len(solution_set.keys())!=height*width:
        row=random.randint(0,height)
        column=random.randint(0,width)
        if (row, column) not in solution_set:
            yield (row, column)

def can_color_be_assigned_here(color, coordinates, solve_dict,height,width):

    return(get_four_neighbors_colors(solve_dict, color, coordinates, height, width))

    #For this function, I need to check the various basic constraints. The first thing to do is to ses
    #If the surrounding squares have either:
    # 2 Blank, or 1 Blank and 1 Same, or no blank and 2 same
    #So First, call get four_neighbors_colors!







def get_four_neighbors(coordinates,height,width):
    neighbors=[]
    #UP neighbor
    if coordinates[0]>0:
        neighbors.append((coordinates[0]-1,coordinates[1]))
    else:
        neighbors.append(None)
    #Down neighbor
    if coordinates[0]<(height-1):
        neighbors.append((coordinates[0]+1, coordinates[1]))
    else:
        neighbors.append(None)
    #Left Neighbor
    if coordinates[1]>0:
        neighbors.append((coordinates[0], coordinates[1]-1))
    else:
        neighbors.append(None)
    #Right Neighbor
    if coordinates[1] < (width-1):
        neighbors.append((coordinates[0], coordinates[1]+1))
    else:
        neighbors.append(None)

    return(neighbors)

def get_four_neighbors_colors(solve_dict,color,coordinates,height,width):
    neighbors=get_four_neighbors(coordinates,height,width)
    ncount = 0
    scount = 0

    for sq in neighbors:
        if sq==None:
            ncount+=1
        else:
            testcolor=solve_dict[sq]
            if testcolor==color:
                scount+=1

    if scount+ncount>=2:
        return(True)
    else:
        return(False)
