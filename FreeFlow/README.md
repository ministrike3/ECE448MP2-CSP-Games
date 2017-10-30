General:
The constraint on pipe_consistency can be tightened 
_______

Smart:

UPDATE: MUST IMPLEMENT FORWARD CHECKING IT ACTUALLY MAKES SENSE OVER THE REST OF THEM

Keep track of remaining legal values for unassigned variables
Terminate search when any variable has no legal values




Most Constrained Variable/Minimum Remaining Values:
The next square to assign is the Sqaure with least number of legal values allowed

Most Constraining Variable:
The next square to choose is the one that has the most constraints on remaining variables
You can use this as a tiebreaker against the Minimum remaining values 

Least Constraining Assignment:
Given a square, in what order should I try the colors?
The color that rules out the fewest colors in the remaining squares


Arc Consistency

ARC CONSISTENCY LOOKS HARD 
