# Welcome to my repo for AI-LAB
  This repo contains Artifical Intelligence Algorithms
  

- __Solving 8puzzle using Astar Algorithm__
  Using Two different Heuristics 

## astarwithh1.py - 
Using heuristics h1 for solving the 8puzzle.

f(s) = g(s) + h(s)

where
g(s) = sum of accrued costs from the start to the current node
h(s) = Number of misplaced squares/numbers in the puzzle to solution. 


### astarwithh2.py - 
using heuristics h2 manhattan distance to solve the 8 puzzle.

the h(s) is for every square the horizontal and vertical distances to that square's location in the goal state are added together. This value is then summed over all squares.

