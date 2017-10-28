# In This file write all the processing Functions
import random


def get_next_variable_to_assign(solution_set,height,width):
    #returns a 2-D tuple of (row, column) that DOES NOT already exist in the solution set
    while len(solution_set.keys())!=height*width:
        row=random.randint(0,height)
        column=random.randint(0,width)
        if (row, column) not in solution_set:
            yield (row, column)

def can_color_be_assigned_here(color, coordinates, solve_dict)):
    pass



def smart_implementation():
    pass


#It's important to avoid the possibility of forming invalid "loops" of pipe.
# One way to do this is by maintaining, for each allowed colour i of each square x, 2 bits of information:
# whether the square x is connected by a path of definite i-coloured tiles to the first i-coloured endpoint,
# and the same thing for the second i-coloured endpoint.

# Then when recursing, don't ever pick a square that has two neighbours with the
# same bit set (or with neither bit set) for any allowed colour.]
