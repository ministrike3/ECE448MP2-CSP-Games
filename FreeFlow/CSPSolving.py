# In This file write all the processing Functions

def dumb_implementation():
#Thoughts

#For every empty square, form a set of possible colours for that square, and then repeatedly perform
# logical deductions at each square to shrink the allowed set of colours for that square.

#Whenever a square's set of possible colours shrinks to size 1, the colour for that square is determined.

#If there are no more squares with logical deductions to perform and the puzzle is not completely solved yet
# because some squares have more than one possibilty left,  pick one of these undecided squares
# and recurse on it, trying each of the possible colours in turn.

# Each try will either lead to a solution, or a contradiction.
# If contradiction eliminate that colour as a possibility for that square.

#When picking a square to branch on, it's generally a good idea to pick a square with
# as few allowed colours as possible.

#It's important to avoid the possibility of forming invalid "loops" of pipe.
# One way to do this is by maintaining, for each allowed colour i of each square x, 2 bits of information:
# whether the square x is connected by a path of definite i-coloured tiles to the first i-coloured endpoint,
# and the same thing for the second i-coloured endpoint.

# Then when recursing, don't ever pick a square that has two neighbours with the
# same bit set (or with neither bit set) for any allowed colour.]

    pass



def smart_implementation():
    pass