# In This file write all the processing Functions
# (row,column)
import random


def get_next_variable_to_assign(solution_set,height,width):
    #returns a 2-D tuple of (row, column) that DOES NOT already exist in the solution set
    # if len(solution_set.keys())!=height*width:
    #     while len(solution_set.keys())!=height*width:
    #         row=random.randint(0,height-1)
    #         column=random.randint(0,width-1)
    #         if (row, column) not in solution_set:
    #             yield (row, column)

    for row in range(height):
        for column in range(width):
            if (row, column) not in solution_set:
                yield (row, column)

def can_color_be_assigned_here(color, coordinates, solve_dict,height,width,initial_points):

    for_location = get_four_neighbors_colors(solve_dict, color, coordinates, height, width)
    if for_location == False:
        return (False)

    neighboring_squares=get_four_neighbors(coordinates,height,width)

    for square in neighboring_squares:
        if square != None:
            if square not in initial_points.keys():
                for_this_square=get_four_neighbors_colors(solve_dict, color, square, height, width)
                if for_this_square==False:
                    return(False)

    for square in initial_points.keys():
        for_this_initial=get_four_neighbors_colors_initial(solve_dict, initial_points[square], square, height, width)
        if for_this_initial==False:
            return(False)

    for square in solve_dict.keys():
        goodspot=is_this_a_good_spot(solve_dict,solve_dict[square],square,height,width)
        if goodspot==False:
            return(False)

    return(True)

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
    no_sq_count = 0
    same_count = 0
    diff_count = 0

    for sq in neighbors:
        if sq==None:
            no_sq_count+=1
        else:
            if sq in solve_dict.keys():
                testcolor = solve_dict[sq]
                if testcolor == color:
                    same_count += 1
                if testcolor != color:
                    diff_count += 1

    if no_sq_count == 2:
        # If it has 2 neighbors
        # Then it is true if both are the same color as it, if 1 is the same and one is blank, or both are blank
        if diff_count == 0:
            return(True)
        return(False)

    if no_sq_count == 1:
        # if 2 are the same, if 1 is the same and there is 1 or 2 blanks, if 0 are the same but there are 2 blanks

        # Ensure its false if all 3 are the same
        if same_count==3:
            return(False)
        # This case covers if 2 are the same; this is allowed
        elif same_count == 2:
            return(True)
        # This case covers if 1 is the same and there are 1 or 2 blanks
        elif same_count == 1:
            if diff_count<=1:
                return(True)
        #This case covers if 0 are the same but there are 2 blanks
        elif  same_count==0:
            if diff_count<=1:
                return(True)
        return(False)

    if no_sq_count == 0:
        # IF it has 4 neighbors, then it is ok to color if
        # 2+ Blank, or 1/2 Blank and 1/2 Same, or no blank and 2 same but not 3 same
        if same_count == 4:
            return (False)

        elif same_count == 3:
            return (False)

        elif same_count == 2:
            return (True)

        elif same_count <= 1:
            if diff_count < 3:
                return(True)
            return (False)

def get_four_neighbors_colors_initial(solve_dict,color,coordinates,height,width):
    neighbors=get_four_neighbors(coordinates,height,width)
    no_sq_count = 0
    same_count = 0
    diff_count = 0

    for sq in neighbors:
        if sq==None:
            no_sq_count+=1
        else:
            if sq in solve_dict.keys():
                testcolor = solve_dict[sq]
                if testcolor == color:
                    same_count += 1
                if testcolor != color:
                    diff_count += 1

    if no_sq_count == 2:
        # If it has 2 neighbors
        #if both are the same colors its false
        if same_count == 2:
            return(False)
        #if one is the same color, it doesnt matter whether the other is colored or blank, its True
        elif same_count == 1:
            return(True)
        #if there are none of the same color, run a check
        elif same_count == 0:
            #If, of the 2 squares, 0 or 1 are different colors then this one, then one or 2 are blank and this is ok
            if diff_count < 2:
                return(True)
            #otherwise this is false
            return(False)

    if no_sq_count == 1:
        # if it has 3 neighbors
        if same_count == 3:
            return(False)
        elif same_count == 2:
            return(False)
        elif same_count == 1:
            return(True)
        else:
            #if at least one has been left blank, then this is ok
            if diff_count < 3:
                return(True)
            return(False)

    if no_sq_count == 0:
        # IF it has 4 neighbors
        if same_count == 4:
            return (False)
        if same_count == 3:
            return (False)
        if same_count == 2:
            return (False)
        if same_count == 1:
            return (True)
        if same_count == 0:
            if diff_count < 4:
                return(True)
            return(False)

def is_this_a_good_spot(solve_dict,color,coordinates,height,width):
    neighbors=get_four_neighbors(coordinates,height,width)
    no_sq_count = 0
    same_count = 0
    diff_count = 0

    for sq in neighbors:
        if sq==None:
            no_sq_count+=1
        else:
            if sq in solve_dict.keys():
                testcolor = solve_dict[sq]
                if testcolor == color:
                    same_count += 1
                if testcolor != color:
                    diff_count += 1

    if same_count+diff_count==4-no_sq_count:
        if same_count==0:
            return(False)
    return(True)

def zig_zag_check(solve_dict,color,coordinates,height,width):
    pass