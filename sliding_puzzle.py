import numpy as np
from solver import Solver
import sys, getopt

def A_star(init_state, goal_state, max_iter, heuristic):
#goal_state = np.array([[1, 2, 3],
#                       [4, 5, 6],
#                       [7, 8, 0]])
#
#init_state = np.array([[1, 8, 7],
#                       [3, 0, 5],
#                       [4, 6, 2]])
    solver = Solver(init_state, goal_state, heuristic, max_iter)
    path = solver.solve()
    
    if len(path) == 0:
        exit(1)
    
    init_idx = init_state.flatten().tolist().index(0)
    init_i, init_j = init_idx // goal_state.shape[0], init_idx % goal_state.shape[0]
    
    print()
    print('INITIAL STATE')
    for i in range(goal_state.shape[0]):
        print(init_state[i, :]) 
    print()
    for node in reversed(path):
        cur_idx = node.get_state().index(0)
        cur_i, cur_j = cur_idx // goal_state.shape[0], cur_idx % goal_state.shape[0]
        
        new_i, new_j = cur_i - init_i, cur_j - init_j
        if new_j == 0 and new_i == -1:
            print('Moved UP    from ' + str((init_i, init_j)) + ' --> ' + str((cur_i, cur_j)))
        elif new_j == 0 and new_i == 1:
            print('Moved DOWN  from ' + str((init_i, init_j)) + ' --> ' + str((cur_i, cur_j)))
        elif new_i == 0 and new_j == 1:
            print('Moved RIGHT from ' + str((init_i, init_j)) + ' --> ' + str((cur_i, cur_j)))
        else:
            print('Moved LEFT  from ' + str((init_i, init_j)) + ' --> ' + str((cur_i, cur_j)))
        print('Score using ' + heuristic + ' heuristic is ' + str(node.get_score() - node.get_level()) + ' in level ' + str(node.get_level()))
    
        init_i, init_j = cur_i, cur_j
        
        for i in range(goal_state.shape[0]):
            print(np.array(node.get_state()).reshape(3,3)[i, :]) 
        print()
    print(solver.get_summary())

def main(argv):
    max_iter = 5000
    heuristic = "manhattan"
    
    try:
        opts, args = getopt.getopt(argv,"h",["mx=","heur="])
    except getopt.GetoptError:
        print('python sliding_puzzle.py --mx <maximum_nodes> --heur <heuristic>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('python sliding_puzzle.py --mx <maximum_nodes> --heur <heuristic>')
            sys.exit()
        elif opt in ("--mx"):
            max_iter = int(arg)
        elif opt in ("--heur"):
            if arg == "manhattan" or arg == "misplaced_tiles":
                heuristic = (arg)
    
    while True:
        try:
            init_state = input("Enter a list of 9 numbers representing the inital state, SEPERATED by WHITE SPACE(1 2 3 etc.): ")
            init_state = init_state.split() 
            for i in range(len(init_state)):
                init_state[i] = int(init_state[i])
            goal_state = input("Enter a list of 9 numbers representing the goal state, SEPERATED by WHITE SPACE(1 2 3 etc.): ")
            goal_state = goal_state.split()
            for i in range(len(goal_state)):
                goal_state[i] = int(goal_state[i])
            if len(goal_state) == len(init_state) and len(goal_state) == 9:
                break
            else:
                print("Please re-enter the input again correctly")
        except Exception as ex:
            print(ex)
            
    init_state = np.array(init_state).reshape(3, 3)
    goal_state = np.array(goal_state).reshape(3, 3)
    
    A_star(init_state, goal_state, max_iter, heuristic)
    
if __name__ == "__main__":
    main(sys.argv[1:])
