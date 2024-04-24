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
        current_energy = int(start_state.evaluation())

        T = 1000
        while T > 0.1:
            neighbors = []
            T = schedule(T)
            
            for neighbor in start_state.get_neighbors():
                neighbors.append(neighbor)

            if len(neighbors) == 0 or T == 0:
                break
            
            next_state = start_state.random_neighbors(neighbors)
            next_energy = int(next_state.evaluation())
            delta_e = next_energy - current_energy
            if delta_e > 0 or random.random() < math.exp(delta_e / T):
                start_state = next_state 
                current_energy = next_energy
            else:
                break
            
        return start_state.find_path()


    def local_beam_search(problem, k):
        current_state = [problem]
        best_path = []
        while True:
            neighbors = []
            neighbors_state = []
            
            for state in current_state:
                for neighbor in state.get_neighbors():
                    if neighbor.state_start not in neighbors_state:
                        neighbors.append(neighbor)
                        neighbors_state.append(neighbor.state_start)
            
            if current_state[0].parent != None:
                state = current_state[0].parent
            else:
                state = current_state[0]
            
            current_state = sorted(neighbors, key=lambda problem: problem.evaluation(), reverse=True)[:k]
            if current_state[0].state_start == state.state_start and current_state[0].evaluation() <= state.evaluation():
                best_path = state.find_path()
                break
        
        return best_path




