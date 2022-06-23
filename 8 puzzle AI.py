import queue
import sys, copy
import time

# Below are some built in puzzles for quick testing.
goal = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']]
trivial = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']]
veryEasy =[['1', '2', '3'], ['4', '5', '6'], ['7', '0', '8']]
easy = [['1', '2', '0'], ['4', '5', '3'], ['7', '8', '6']]
doable = [['0', '1', '2'], ['4', '5', '3'], ['7', '8', '6']]
oh_boy = [['8','7','1'],['6','0','2'],['5','4','3']]
default = [['1', '2', '3'], ['4', '0', '6'], ['7', '5', '8']]

def main():
    puzzle = []
    while True:
        # Choose a default puzzle
        puzzle_mode = input("Welcome to an 8-Puzzle Solver. Type '1' to use a default puzzle, or '2' to create your own.\n")
        if (puzzle_mode == "1"):
            puzzle = init_default_puzzle_mode()
        # Enter a puzzle by user
        elif (puzzle_mode == "2"):
            print("Enter your puzzle, use a zero to represent the blank. Please Enter Valid 8-Puzzles.Use space between two numbers:\n")
            firstrow = input("Enter the first row: \n")
            firstrow = firstrow.split(' ')
            secondrow = input("Enter the second row: \n ")
            secondrow = secondrow.split(' ')
            thirdrow = input("Enter the third row :\n")
            thirdrow = thirdrow.split(' ')
            puzzle.append(firstrow)
            puzzle.append(secondrow)
            puzzle.append(thirdrow)
            print("\n")
        # Choose between 3 Algorithms.    
        queueing_function = select_and_init_algorithm(puzzle) 
        # Start the puzzle search
        general_search(puzzle, queueing_function)         
def init_default_puzzle_mode():
    # This function allows user to create default puzzle.
    print("1.Trivial")
    print("2.VeryEasy")
    print("3.Easy")
    print("4.Doable")
    print("5.Oh Boy")
    print("6.Default")
    print("\n")
    selected_difficulty = input("You wish to use a default puzzle. Please enter a desired difficulty on a scale from 1 to 6." + '\n')
    if selected_difficulty == "1":
        print("Difficulty of 'Trivial' selected.")
        return trivial
    if selected_difficulty == "2":
        print("Difficulty of 'VeryEasy' selected.")
        return veryEasy
    if selected_difficulty == "3":
        print("Difficulty of 'Easy' selected.")
        return easy
    if selected_difficulty =="4":
        print("Difficulty of 'Doable' selected.")
        return doable
    if selected_difficulty == "5":
        print("Difficulty of 'Oh Boy' selected.")
        return oh_boy
    if selected_difficulty == "6":
        print("Difficulty of 'Default' selected.")
        return default
def select_and_init_algorithm(puzzle):
    # This function allows user to select between 3 algorithms.
    Algo = (input('Select Algorithm. \n(1)For  Uniform Cost Search.\n(2)For A* with the misplaced Tile heuristic.\n(3)For A* with the Manhattan distance heuristic distance heuristic\n'))
    return Algo

def expand(puzzle,visited):
    # Resource for copy,deepcopy:https://docs.python.org/3/library/copy.html
    # This function finds children of a node.
    child_nodes=[]  # stores four children by moving 0's
    # take a copy of the puzzle
    left = copy.deepcopy(puzzle.puzzle)
    # Move 0 to left
    for ind,val in enumerate(left):
        # looping throw the rows of left.
        if (val.count('0') == 1):
            # finding the row of 0
            if (val.index('0')!= 0): # checking that 0 is not in 1st column. Only them 0 can be moved left.
                # Swapping 0 with left element in puzzle.
                tile_zero = val.index('0')
                left[ind][tile_zero],left[ind][tile_zero-1]=left[ind][tile_zero-1],left[ind][tile_zero]
                child_node=node(left)
                child_node.path_cost=puzzle.path_cost+1
                # Checking if the puzzle is already visited. If its visited, We need not visit it again.
                if left not in visited:
                    child_nodes.append(child_node)
                break

    # take a copy of the puzzle
    right = copy.deepcopy(puzzle.puzzle)
    # Move 0 to right
    for ind,val in enumerate(right):
        # looping throw the rows of right.
        if (val.count('0') == 1):
            # finding the row of 0
            if (val.index('0') != 2): # checking that 0 is not in the 3rd column. Only them it can moved right
                # Swapping 0 with right element in the puzzle.
                tile_zero = val.index('0')
                right[ind][tile_zero],right[ind][tile_zero+1]=right[ind][tile_zero+1],right[ind][tile_zero]
                child_node=node(right)
                child_node.path_cost=puzzle.path_cost+1
                # Checking if the puzzle is already visited. If its visited, We need not visit it again.
                if right not in visited:
                    child_nodes.append(child_node)
                break
    # take a copy of the puzzle
    top = copy.deepcopy(puzzle.puzzle)
    # Move 0 to top
    for ind,val in enumerate(top):
        # looping throw the rows of top.
        if (val.count('0') == 1):     
             # finding the row of 0   
            if (val != top[0]):   # checking that 0 is not in the 1st row. Only them it can moved top
                # Swapping 0 with top element in the puzzle.
                tile_zero = val.index('0')
                top[ind][tile_zero],top[ind-1][tile_zero]=top[ind-1][tile_zero],top[ind][tile_zero]
                child_node=node(top)
                child_node.path_cost=puzzle.path_cost+1
                # Checking if the puzzle is already visited. If its visited, We need not visit it again.
                if top not in visited:
                    child_nodes.append(child_node)
                break
    # take a copy of the puzzle
    bottom = copy.deepcopy(puzzle.puzzle)
    # Move 0 to bottom
    for ind,val in enumerate( bottom):
        # looping throw the rows of bottom.
        if (val.count('0') == 1):
            if (val != bottom[2]):   # checking that 0 is not in 3rd row.Only them it can be moved top
                # Swapping 0 with bottom element in the puzzle.
                tile_zero = val.index('0')
                bottom[ind][tile_zero], bottom[ind+1][tile_zero]= bottom[ind+1][tile_zero], bottom[ind][tile_zero]
                child_node=node(bottom)
                child_node.path_cost=puzzle.path_cost+1
                # Checking if the puzzle is already visited. If its visited, We need not visit it again.
                if bottom not in visited:
                    child_nodes.append(child_node) 
                break           
    return child_nodes

def misplaced_tiles(puzzle):
    goal_state = [['1', '2', '3'], ['4', '5','6'], ['7', '8','0']]
    count = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] !='0':
                if puzzle[i][j] !=goal_state[i][j]:
                    count+=1
                
    return count  #returns misplaced tileis heuristic value.

def manhattan_distance(puzzle):
    count=0
    goal_state = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']]
    p = []
    g = []
    # making a list of all elements in puzzle.
    for i in puzzle:
        p.extend(i)
    # making a list of all elements in goal state
    for j in goal_state:
        g.extend(j)
    # if puzzle element is not 0 and we calculate count by finding the distance between puzzle tile and 0.
    for goal,puzz in enumerate(p):
        if puzz=='0':
            continue
        else:
            puzz_row,puzz_col = (int(puzz)-1)//3,(int(puzz)-1)%3
            goal_row,goal_col = goal//3,goal%3
            count+=abs(puzz_row-goal_row)+abs(puzz_col-goal_col)
    return count           #returns manhattan distance

def general_search(puzzle, queueing_function):
    start_time=time.time()                    # Calculates start time of the search.
    run_time = 900                            # maximum run time of the problem is 15 mins = 900 secs.
    nodes_expanded = 0                        # calculates expanded nodes.
    max_queue_size = 0                        # calculates maximum size of queue at any point.
    queue = []                                # creating a queue data structure.
    visited = []                              # stores all the explored nodes, to decrease the search space.
    initial_node = node(puzzle)                 # a puzzle node object is created.
    initial_node.path_cost = 0                  # initial depth is 0.
    queue.append(initial_node)                  # initial node object is added to the queue.
    visited.append(initial_node.puzzle)         # updating visited list
    while True:
        # sorting the queue to get minimum f(n)
        # reference:https://stackoverflow.com/questions/3766633/how-to-sort-with-lambda-in-python
        queue=sorted(queue,key=lambda x :(x.path_cost+x.heuristic_cost,x.path_cost))
        # checking is queue is empty. If queue is empty, search is over.
        if (len(queue) == 0):
          print("Search is Over")
          sys.exit(0)
        # pop the first node from queue.
        popped_node =queue.pop(0)
        # Printing the best node to expand using sorting we choose best node.
        print ("The best node with least f(n) to expand with is a g(n) =", popped_node.path_cost,"and h(n) =", popped_node.heuristic_cost)
        print(popped_node.puzzle[0][0], popped_node.puzzle[0][1], popped_node.puzzle[0][2])
        print(popped_node.puzzle[1][0], popped_node.puzzle[1][1], popped_node.puzzle[1][2])
        print(popped_node.puzzle[2][0], popped_node.puzzle[2][1], popped_node.puzzle[2][2])
        print("Expanding Node")
        # check if we reached goal state.  We print the depth and heuristic of value is not 0, nodes expanded and time taken.
        if (goal == popped_node.puzzle):
            print("Solution Reached!!")
            print(popped_node.puzzle[0][0], popped_node.puzzle[0][1], popped_node.puzzle[0][2])
            print(popped_node.puzzle[1][0], popped_node.puzzle[1][1], popped_node.puzzle[1][2])
            print(popped_node.puzzle[2][0], popped_node.puzzle[2][1], popped_node.puzzle[2][2])            
            print("Problem is Solved in ", nodes_expanded, "nodes")
            print("Maximum number of nodes in the queue at any one time was", max_queue_size)
            print("The depth of the goal node was", popped_node.path_cost)
            #print("Time Taken:",time.time()-start_time)
            print(" Time Taken:{:.2f}".format(time.time()-start_time))
            return
        # stores children of the node.
        expandedPuzzle = expand(popped_node,visited)
        for x in expandedPuzzle:
            # loop through all child nodes.
            # assign the heuristic value according to the algorithm.
            if (queueing_function == '1'):
                x.heuristic_cost = 0
                #tempNode.path_cost=tempNode.path_cost+1
            elif (queueing_function == '2'):
                x.heuristic_cost = misplaced_tiles(x.puzzle)
            else:
                x.heuristic_cost = manhattan_distance(x.puzzle)

            # updating queue with the child node.
            queue.append(x)
            # incrementing count of expanded nodes.
            nodes_expanded += 1
            # updating visited list of nodes.
            visited.append(x.puzzle)
            # updating maximum size of queue everytime.
            max_queue_size=max(len(queue),max_queue_size)
        # if the time exceeds 15 mins, we are breaking the search loop.
        if time.time() > start_time + run_time:
            print('Time Over')
            sys.exit(0)
# Class Node is defined. we define heuristic cost and path cost stores g(n) and h(n) values of each node by creating objects.
class node:
    def __init__(self,puzzle):
        self.puzzle = puzzle
        self.heuristic_cost = 0
        self.path_cost = 0
if __name__ == "__main__":
    main()