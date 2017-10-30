# Things Left for this Part in General: #

The constraint on pipe_consistency can be tightened 

_______

### Smart: ###

Forward checking is complete; the important thing now is to make a smarter choice of which node to expand next

** Most Constrained Variable/Minimum Remaining Values: **

The next square to assign is the Sqaure with least number of legal values allowed

** Most Constraining Variable: **

The next square to choose is the one that has the most constraints on remaining variables

You can use this as a tiebreaker against the Minimum remaining values 

** Least Constraining Assignment: **

Given a square, in what order should I try the colors?

The color that rules out the fewest colors in the remaining squares

### Arc Consistency ###

** ARC CONSISTENCY LOOKS HARD ** 
