from queue import PriorityQueue
from game_state import GameState
import numpy as np
import time

class Solver():
    def __init__(self, init_state, goal_state, heuristic_func = "manhattan", max_iter = 2500):
        self.__init_state = init_state
        self.__goal_state = goal_state
        self.__heuristic_func = heuristic_func
        self.__MAX = 100000
        self.__max_iter = max_iter
        self.__path = []
        self.__number_of_steps = 0
        self.__summary = ""
        
    def set_max_iter(self, max_iter):
        self.__max_iter = max_iter
        
    def get_path(self):
        return self.__path
    
    def get_summary(self):
        return self.__summary
        
    def solve(self):
        x_axis = [1, 0, -1,  0]
        y_axis = [0, 1,  0, -1]
        
        level = 0
        visited_nodes = set()
        
        start_time = time.clock()
        
        nodes = PriorityQueue(self.__MAX)
        init_node = GameState(self.__init_state.flatten().tolist(), self.__goal_state.flatten().tolist(), level, parent = None, heuristic_func = self.__heuristic_func)
        nodes.put(init_node)
        
        epochs = 0
        while nodes.qsize() and epochs <= self.__max_iter:
            epochs += 1
            
            cur_node = nodes.get()
            cur_state = cur_node.get_state()
            
            if str(cur_state) in visited_nodes:
                continue
            visited_nodes.add(str(cur_state))
            
            if cur_state == self.__goal_state.flatten().tolist():
                self.__summary = str("A* took " + str(cur_node.get_level()) + " steps to get from initial state to the desired goal, visited total of " + str(epochs) + " nodes, and took around " + str(np.round(time.clock() - start_time, 4)) + " seconds to reach the desired solution.")
                while cur_node.get_parent():
                    self.__path.append(cur_node)
                    cur_node = cur_node.get_parent()
                break
            
            empty_tile = cur_state.index(0)
            i, j = empty_tile // self.__goal_state.shape[0], empty_tile % self.__goal_state.shape[0]
            
            cur_state = np.array(cur_state).reshape(3, 3)
            for x, y in zip(x_axis, y_axis):
                new_state = np.array(cur_state)
                if i + x >= 0 and i + x <= 2 and j + y >= 0 and j + y <= 2:
                    new_state[i, j], new_state[i+x, j+y] = new_state[i+x, j+y], new_state[i, j]
                    game_state = GameState(new_state.flatten().tolist(), self.__goal_state.flatten().tolist(), cur_node.get_level() + 1, cur_node, self.__heuristic_func)
                    if str(game_state.get_state()) not in visited_nodes:
                        nodes.put(game_state)
        if epochs > self.__max_iter:
            print('This grid setting is not solvable')
        return self.__path