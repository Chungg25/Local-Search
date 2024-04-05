import random
import math
class LocalSearchStrategy:
    def random_restart_hill_climbing(problem, num_trial):
        best_path = None
        best_evaluation = float('-inf') 

        for _ in range(num_trial):
            current_state = problem.random_state()
            while True:
                neighbors = problem.get_neighbors(current_state)
                next_state = max(neighbors, key=lambda x: x[2])
                if next_state[2] <= current_state[2]:
                    break
                current_state = next_state
                if problem.is_goal(next_state):
                    return problem.find_path(next_state)
            if problem.evaluation(current_state[0], current_state[1]) > best_evaluation: 
                best_evaluation = current_state[2]
                best_path = problem.find_path(current_state)
                
        return best_path
    
    def simulated_annealing_search(problem, schedule):
        x, y = problem.state_start
        current_enery = int(problem.evaluation(x, y))
        start_state = (x, y, current_enery, problem)

        if problem.is_goal(start_state): return [(x, y, current_enery)]

        explored = [(start_state[0], start_state[1])]
        T = 2
        while T > 0:
            T = schedule(T)

            if T == 0:
                return problem.find_path(start_state)
            
            neighbor = []
                
            for i in problem.get_neighbors(start_state):
                if (i[0], i[1]) not in explored:
                    neighbor.append(i)

            if len(neighbor) == 0:
                return problem.find_path(start_state)

            next_state = problem.random_neighbors(neighbor)
            explored.append((next_state[0], next_state[1]))
            next_enery = int(problem.evaluation(next_state[0], next_state[1]))
            delta_e = next_enery - current_enery
            
            if delta_e > 0 or random.random() < math.exp(delta_e / T):
                start_state = next_state 
                current_enery = next_enery

        return problem.find_path(start_state)

    def local_beam_search(problem, k):
        x, y = problem.state_start
        current_enery = int(problem.evaluation(x, y))
        current_state = [(x, y, current_enery, problem)]

        state_start = current_state[0]

        if problem.is_goal(state_start): return [(x, y, current_enery)]

        explored = []
        best_path = []
        while True:
            neighbor = []
            for state in current_state:
                for i in problem.get_neighbors(state):
                    if (i[0], i[1]) not in explored:
                        neighbor.append(i)
            
            if len(neighbor) == 0:
                best_path = problem.find_path(current_state[0])
                break

            current_state = sorted(neighbor, key=lambda x: x[2], reverse=True)[:k]
            
            for i in current_state:
                explored.append((i[0], i[1]))

            for state in current_state:
                if problem.is_goal(state):
                    return problem.find_path(state)
                
        return best_path





