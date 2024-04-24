from problem import Problem
from search import LocalSearchStrategy
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--search-strategy', type=str, help='Search stategy')
parser.add_argument('-p', '--path', type=str, help='Path to problem image')
parser.add_argument('-c', '--coordinates', nargs='+', type=int, help='a list of coordinates seperated by space')

args = parser.parse_args()

if args.path:
    file_path = args.path
    
if args.search_strategy:
    search_strategy = args.search_strategy
    
if args.coordinates:
    start_state = tuple(args.coordinates)


def schedule(T):
    return T * 0.95

def test_hill_climbing(title, problem_path='monalisa.jpg'):
    problem = Problem(problem_path)
    best_path = LocalSearchStrategy.random_restart_hill_climbing(problem, 5)
    if best_path:
        problem.draw_path(best_path, title)

def test_local_beam_search(title, problem_path='monalisa.jpg', default_start_state=(40, 0)):
    problem = Problem(problem_path, state_start=default_start_state)
    best_path = LocalSearchStrategy.local_beam_search(problem, 5)
    if best_path:
        problem.draw_path(best_path, title)

def test_simulated_annealing_search(title, problem_path='monalisa.jpg', default_start_state=(40, 0)):
    problem = Problem(problem_path, state_start=default_start_state)
    best_path = LocalSearchStrategy.simulated_annealing_search(problem, schedule)
    if best_path:
        problem.draw_path(best_path, title)

if search_strategy.lower() == 'rrhc':
    test_hill_climbing('Random restart hill climbing', file_path)
elif search_strategy.lower() == 'sas':
    test_simulated_annealing_search('Simulated annealing search', file_path, start_state)
elif search_strategy.lower() == 'lbs':
    test_local_beam_search('Local beam search', file_path, start_state)
    
