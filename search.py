import random
import math
class LocalSearchStrategy:
    def random_restart_hill_climbing(problem, num_trial):
        best_path = None
        best_evaluation = float('-inf') 

        for _ in range(num_trial):
            current_state = problem.random_state()
            path = [(current_state[0], current_state[1], current_state[2])]
            while True:
                neighbors = problem.get_neighbors(current_state)
                next_state = max(neighbors, key=lambda x: x[2])
                if next_state[2] <= current_state[2]:
                    break
                current_state = next_state
                path.append((current_state[0], current_state[1], current_state[2]))
            if problem.evaluation(current_state[0], current_state[1]) > best_evaluation: 
                best_evaluation = current_state[2]
                best_path = path
        
        return best_path
    
    def simulated_annealing_search(problem, schedule):
        current_state = [problem.random_state()]
        start_state = current_state[0]
        current_enery = int(problem.evaluation(current_state[0][0], current_state[0][1]))
        path = [(current_state[0][0], current_state[0][1], current_state[0][2])]
        explored = [(current_state[0][0], current_state[0][1], current_state[0][2])]
        neighbor = []
        flag = False
        T = 2
        while T > 0:
            T = schedule(T)
            if T == 0:
                return path
            
            if flag:
                neighbor = []
                explored = []
                
            for i in problem.get_neighbors(start_state):
                if (i[0], i[1], i[2]) not in explored:
                    neighbor.append(i)
                    explored.append((i[0], i[1], i[2]))
            
            next_state = problem.random_neighbors(neighbor)
            next_enery = int(problem.evaluation(next_state[0], next_state[1]))
            delta_e = next_enery - current_enery
            
            if delta_e > 0 or random.random() < math.exp(delta_e / T):
                start_state = next_state 
                current_enery = next_enery
                path.append((start_state[0], start_state[1], start_state[2]))
                continue
            flag = True

        return path

    def local_beam_search(problem, k):
        best_path = []
        current_state = [problem.random_state()]
        state_start = current_state[0]
        explored = []
        while True:
            neighbor = []
            for state in current_state:
                for i in problem.get_neighbors(state):
                    if (i[0], i[1], i[2]) not in explored:
                        neighbor.append(i)
                        explored.append((i[0], i[1], i[2]))

            if len(neighbor) == 0:
                best_path = problem.find_path(current_state[0], state_start)
                break

            current_state = sorted(neighbor, key=lambda x: x[2], reverse=True)[:k]

            if problem.is_goal(current_state):
                goal = problem.find_goal(current_state)
                best_path = problem.find_path(goal, state_start)
                break
                
        return best_path





