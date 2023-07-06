# Eight_Puzzle_Solver

## Table Of Contents:
   * [Abstract](#Abstract)
   * [Uniform Cost Search](#Uniforme-Cost-Search)
     * [Uniform Cost Search Code Above Explained](#Uniform-Cost-Search-Code-Above-Explained)
    * [A* with the misplaced tile heuristic](#A*-with-the-misplaced-tile-heuristic)
      * [Misplaced Tile Heuristic Code Explained](#Misplaced-Tile-Heuristic-Code-Explained)
    * [A* with the Manhattan distance heuristic](#A*-with-the-Manhattan-distance-heuristic)
      * [Manhattan Distance Heuristic Code Explained](#Manhattan-Distance-Heuristic-Code-Explained)

![image](https://github.com/madhuammulu8/Eight_Puzzle_Solver/assets/65707202/38a7702d-31e2-4cdc-8792-71d7c1a4720f)

# Abstract

The provided code is an implementation of an 8-Puzzle Solver in Python. It allows the user to solve the 8-Puzzle problem by selecting a default puzzle or creating their own. 
The solver supports three different algorithms: Uniform Cost Search, A* with the misplaced tile heuristic, and A* with the Manhattan distance heuristic

# Uniform Cost Search

Uniform Cost Search is an algorithm used in the 8-Puzzle Solver to find the optimal solution to the puzzle. It explores the search space by considering the cumulative cost 
of each path from the initial state to a particular node. The algorithm starts with the initial state and uses a priority queue to prioritize nodes based on their cumulative costs.
At each step, it selects the node with the minimum cost, generates its child nodes by moving the blank tile in different directions, and calculates the cumulative cost for each child node. 
The algorithm continues this process until it reaches the goal state or exhausts all possible paths. Uniform Cost Search guarantees to find the optimal solution with the lowest cost,
but it can be computationally expensive for large search spaces or when the cost of actions varies widely.

### Uniform Cost Search Code Above Explained

* Initialized the priority queue with the initial state of the puzzle and a cost of 0.
* Initialized an empty set to keep track of visited nodes.
* Repeat until the priority queue is empty
  * Remove the node with the minimum cost from the priority queue.
  * If the removed node is the goal state (i.e., the puzzle configuration matches the desired goal state), return the solution.
  * Add the removed node to the set of visited nodes.
  * Generate all possible child nodes from the current node by moving the blank (represented by '0') in different directions (left, right, up, down).
  * For each child node:
    * If the child node has not been visited, calculate its cumulative cost by adding the cost of the current node and the cost to reach the child node. In Uniform Cost Search, the cost to reach a child node is always 1.
    * Add the child node to the priority queue with its cumulative cost.
* If the priority queue becomes empty without finding the goal state, then there is no solution.

# A* with the misplaced tile heuristic
The misplaced_tiles heuristic is used in the 8-Puzzle Solver as part of the A* search algorithm to estimate the distance from a given puzzle configuration to the goal state. 
This heuristic calculates the number of tiles that are not in their correct positions in the current puzzle configuration. 
By counting the misplaced tiles, the heuristic provides an estimate of how far the current configuration is from the goal state. 
The idea is that the fewer misplaced tiles there are, the closer the configuration is to the goal.
However, it's important to note that the misplaced_tiles heuristic may not always provide an accurate estimate, as it does not consider the actual distance or moves required to reach the goal state. Nonetheless, 
it can be a useful heuristic in guiding the search process and potentially improving the efficiency of finding a solution in some cases.

### Misplaced Tile Heuristic Code Explained

* The misplaced_tiles function calculates the number of misplaced tiles in a given puzzle configuration, serving as a heuristic for the A* search algorithm.
* It takes the current puzzle configuration as input.
* The goal_state variable is defined as the desired goal state of the puzzle.
* The function initializes a count variable to keep track of the number of misplaced tiles.
* Using nested loops, the function iterates over each element in the puzzle configuration and the goal state.
* For each element, except the blank tile ('0'), the function compares the tile in the puzzle configuration with the corresponding tile in the goal state.
* If the tiles are not equal, it means that the tile is misplaced, and the count variable is incremented.
* Finally, the function returns the count, representing the total number of misplaced tiles in the given puzzle configuration.

# A* with the Manhattan distance heuristic
The Manhattan distance heuristic is an important component of the 8-Puzzle Solver, particularly in the A* search algorithm. 
This heuristic is used to estimate the distance between the current puzzle configuration and the goal state. 
It calculates the total number of horizontal and vertical moves required to move each tile from its current position to its goal position in the puzzle.
By summing up these distances for all tiles, the Manhattan distance heuristic provides an estimate of how far the current configuration is from the goal state. 
This heuristic takes into account the spatial relationships between the tiles and provides a more informed estimate compared to the misplaced_tiles heuristic. 
The Manhattan distance heuristic is effective in guiding the search process and can lead to more efficient and optimal solutions in the 8-Puzzle problem.

### Manhattan Distance Heuristic Code Explained

* The Manhattan_distance function calculates the Manhattan distance heuristic value for a given puzzle configuration.
* It takes the current puzzle configuration as input.
* The function initializes a count variable to keep track of the Manhattan distance.
* The goal_state variable is defined as the desired goal state of the puzzle.
* Two empty lists, p, and g, are created to store the elements of the puzzle configuration and the goal state, respectively.
* Using nested loops, the function iterates over each element in the puzzle configuration and the goal state.
* For each element, except the blank tile ('0'), the function calculates the row and column indices of the element in both the puzzle configuration and the goal state.
* It then adds the absolute difference between the row indices and column indices to the count variable, representing the Manhattan distance for that particular tile.
* Finally, the function returns the count, which represents the total Manhattan distance for the given puzzle configuration.
