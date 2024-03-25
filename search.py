

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
    
    # def simulated_annealing_search(problem, schedule):
    #     best_path = None
    #     best_evaluation = float('-inf') 

    #     T = schedule
    #     while T > 0:

    def local_beam_search(problem, k):
        best_path = []
        best_evaluation = float('-inf') 
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
                print('1')
                goal = problem.find_goal(current_state)
                best_path = problem.find_path(goal, state_start)
                break
                
        return best_path





