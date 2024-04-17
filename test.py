from problem import Problem
from search import LocalSearchStrategy


def schedule(T):
    return T * 0.9

def test_hill_climbing(title):
    problem = Problem('monalisa.jpg')
    best_path = LocalSearchStrategy.random_restart_hill_climbing(problem, 5)
    print(best_path)
    if best_path:
        problem.draw_path(best_path, title)

def test_local_beam_search(title):
    problem = Problem('monalisa.jpg', state_start=(0, 0))
    best_path = LocalSearchStrategy.local_beam_search(problem, 5)
    print(best_path)
    if best_path:
        problem.draw_path(best_path, title)

def test_simulated_annealing_search(title):
    problem = Problem('monalisa.jpg', state_start=(40, 45))
    best_path = LocalSearchStrategy.simulated_annealing_search(problem, schedule)
    print(best_path)
    if best_path:
        problem.draw_path(best_path, title)


# test_hill_climbing('hill_climbing')
# test_simulated_annealing_search('simulated_annealing_search')
test_local_beam_search('local_beam_search')



