# Sliding Puzzle (NxN) Solver
Implementation for **A-star and BFS Algorithms** to solve a NxN grid sliding puzzle problem.

![State Space.](https://github.com/YahyaAlaaMassoud/Sliding-Puzzle-A-Star-Solver/blob/master/images/state%20space.jpg
"State Space")

### GameState - Class:
**GameState** class describes any game state in the search space. It takes the following arguments: the ***Current State*** as a list, ***Goal State*** as a list, ***Current Level***, ***Parent State***, and the used ***Heuristic Function***, and once it is initialized, the heuristic score is computed for the current state according to the specified fitness function.
```python
# heuristics that can be used are either "manhattan" for manhattan distance or "misplaced_tiles"
game_state = GameState(initial_state, goal_state, level, parent, heuristic_function)
```

<hr/>

### Solver - Class:
**Solver** class is used to solve a specific grid setting. It takes the following arguments: the ***Initial State*** of the grid as a NxN matrix, ***Goal State*** as a NxN matrix, the used ***Heuristic Function***, and the ***Maximum Number of Nodes*** that can be visited during the search.</br>
```python
import numpy as np
goal_state = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 0]])

init_state = np.array([[1, 8, 7],
                       [3, 0, 5],
                       [4, 6, 2]])
heuristic = "manhattan"
max_iter = "10000"
solver = Solver(init_state, goal_state, heuristic, max_iter)
```
It has two functions: **solve_a_star()** and **solve_bfs**, and both function return the path from the initial state to the goal state if the goal state has been reached, or return an empty list if the goal state has not been reached.</br>
```python
path_a_star = solver.solve_a_star()
path_bfs = solver.solve_bfs()
```
It has also a function called **get_summary()** that returns a string describing how many steps took the algorithm to reach the goal state from the specified initial state, how many node the algorithm has visited during the search, and the time the algorithm took to solve the initial grid setting.

<hr/>

### How to solve a specific grid setting using the program
Firstly clone the project
```
git clone https://github.com/YahyaAlaaMassoud/Sliding-Puzzle-A-Star-Solver.git
cd Sliding-Puzzle-A-Star-Solver
```
The program takes several arguments as input to solve a specific grid setting:
 - The shape of the grid (N).
 - The maximum number of nodes that the algorithm can visit during the search space.
 - Heuristic function that will be used to evaluate every game state.
 - Solving the grid setting using either A-star or BFS.
 - You can used -h for Help.
```
python sliding_puzzle.py -h <help> -n <matrix shape ex: n = 3 -> 3x3 matrix> --mx <maximum_nodes> --heur <heuristic> --astar (default algorithm) or --bfs
```
Example of input:
```
python sliding_puzzle.py -n 3 --mx 10000 --heur manhattan --astar
Enter a list of 9 numbers representing the inital state, SEPERATED by WHITE SPACE(1 2 3 etc.): 
1 8 7 3 0 5 4 6 2
Enter a list of 9 numbers representing the goal state, SEPERATED by WHITE SPACE(1 2 3 etc.): 
1 2 3 4 5 6 7 8 0
```
Output:
```
INITIAL STATE
[1 8 7]
[3 0 5]
[4 6 2]

Moved UP    from (1, 1) --> (0, 1)
Score using manhattan heuristic is 18 in level 1
[1 0 7]
[3 8 5]
[4 6 2]

Moved RIGHT from (0, 1) --> (0, 2)
Score using manhattan heuristic is 16 in level 2
[1 7 0]
[3 8 5]
[4 6 2]

Moved DOWN  from (0, 2) --> (1, 2)
Score using manhattan heuristic is 16 in level 3
[1 7 5]
[3 8 0]
[4 6 2]

Moved DOWN  from (1, 2) --> (2, 2)
Score using manhattan heuristic is 14 in level 4
[1 7 5]
[3 8 2]
[4 6 0]

Moved LEFT  from (2, 2) --> (2, 1)
Score using manhattan heuristic is 14 in level 5
[1 7 5]
[3 8 2]
[4 0 6]

Moved UP    from (2, 1) --> (1, 1)
Score using manhattan heuristic is 14 in level 6
[1 7 5]
[3 0 2]
[4 8 6]

Moved UP    from (1, 1) --> (0, 1)
Score using manhattan heuristic is 14 in level 7
[1 0 5]
[3 7 2]
[4 8 6]

Moved RIGHT from (0, 1) --> (0, 2)
Score using manhattan heuristic is 12 in level 8
[1 5 0]
[3 7 2]
[4 8 6]

Moved DOWN  from (0, 2) --> (1, 2)
Score using manhattan heuristic is 10 in level 9
[1 5 2]
[3 7 0]
[4 8 6]

Moved DOWN  from (1, 2) --> (2, 2)
Score using manhattan heuristic is 8 in level 10
[1 5 2]
[3 7 6]
[4 8 0]

Moved LEFT  from (2, 2) --> (2, 1)
Score using manhattan heuristic is 10 in level 11
[1 5 2]
[3 7 6]
[4 0 8]

Moved UP    from (2, 1) --> (1, 1)
Score using manhattan heuristic is 10 in level 12
[1 5 2]
[3 0 6]
[4 7 8]

Moved LEFT  from (1, 1) --> (1, 0)
Score using manhattan heuristic is 10 in level 13
[1 5 2]
[0 3 6]
[4 7 8]

Moved DOWN  from (1, 0) --> (2, 0)
Score using manhattan heuristic is 8 in level 14
[1 5 2]
[4 3 6]
[0 7 8]

Moved RIGHT from (2, 0) --> (2, 1)
Score using manhattan heuristic is 6 in level 15
[1 5 2]
[4 3 6]
[7 0 8]

Moved RIGHT from (2, 1) --> (2, 2)
Score using manhattan heuristic is 4 in level 16
[1 5 2]
[4 3 6]
[7 8 0]

Moved UP    from (2, 2) --> (1, 2)
Score using manhattan heuristic is 6 in level 17
[1 5 2]
[4 3 0]
[7 8 6]

Moved LEFT  from (1, 2) --> (1, 1)
Score using manhattan heuristic is 6 in level 18
[1 5 2]
[4 0 3]
[7 8 6]

Moved UP    from (1, 1) --> (0, 1)
Score using manhattan heuristic is 6 in level 19
[1 0 2]
[4 5 3]
[7 8 6]

Moved RIGHT from (0, 1) --> (0, 2)
Score using manhattan heuristic is 4 in level 20
[1 2 0]
[4 5 3]
[7 8 6]

Moved DOWN  from (0, 2) --> (1, 2)
Score using manhattan heuristic is 2 in level 21
[1 2 3]
[4 5 0]
[7 8 6]

Moved DOWN  from (1, 2) --> (2, 2)
Score using manhattan heuristic is 0 in level 22
[1 2 3]
[4 5 6]
[7 8 0]

Summary: A* took 22 steps to get from initial state to the desired goal, visited total of 670 nodes, and took around 0.2985 seconds to reach the desired solution.
```
