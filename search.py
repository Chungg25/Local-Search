import random
import math
class LocalSearchStrategy:
    def random_restart_hill_climbing(problem, num_trial):
        best_path = None
        best_evaluation = float('-inf') 

        for _ in range(num_trial):

            current_state = problem.random_state()

            while True:
                neighbors = current_state.get_neighbors()

                next_state = max(neighbors, key=lambda problem: problem.evaluation())
                if next_state.evaluation() <= current_state.evaluation():
                    break

                current_state = next_state

            if current_state.evaluation() > best_evaluation: 
                best_evaluation = current_state.evaluation()
                best_path = current_state.find_path()
                
        return best_path
    
    def simulated_annealing_search(problem, schedule):
        start_state = problem
        current_enery = int(start_state.evaluation())
        explored = [problem.state_start]

        T = 1
        while T > 0:
            neighbors = []
            T = schedule(T)
            
            for neighbor in start_state.get_neighbors():
                if neighbor.state_start not in explored:
                    neighbors.append(neighbor)

            if len(neighbors) == 0 or T == 0:
                break
            
            next_state = start_state.random_neighbors(neighbors)
            explored.append(next_state.state_start)
            next_enery = int(next_state.evaluation())
            delta_e = next_enery - current_enery
            
            if delta_e > 0 or random.random() < math.exp(delta_e / T):
                start_state = next_state 
                current_enery = next_enery
            
        return start_state.find_path()

    def local_beam_search(problem, k):
        current_state = [problem]
        explored = [problem.state_start]
        best_path = []

        while True:
            neighbors = []

            for state in current_state:
                for neighbor in state.get_neighbors():
                    if neighbor.state_start not in explored:
                        neighbors.append(neighbor)
            
            state = current_state[0]
            current_state = sorted(neighbors, key=lambda problem: problem.evaluation(), reverse=True)[:k]
            if current_state[0].evaluation() < state.evaluation():
                best_path = state.find_path()
                break

            for state in current_state:
                explored.append(state.state_start)
                
        return best_path





