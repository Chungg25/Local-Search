from problem import Problem
from search import LocalSearchStrategy
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--search-strategy', type=str, help='Search stategy', default='monalisa.jpg')
parser.add_argument('-p', '--path', type=str, help='Path to problem image')
parser.add_argument('-c', '--coordinates', nargs='+', type=int, help='A list contains start coordinate of start state, seperated by space')
parser.add_argument('-n', '--num-trial', type=int, help='Num trial for Random restart hill climbing', default=5)
parser.add_argument('-k', '--maintained-state', type=int, help='an integer, maximum state maintained at each step of Local Beam Search', default=5)

args = parser.parse_args()

if args.path:
    img_path = args.path
else:
    img_path = 'monalisa.jpg'
    
if args.search_strategy:
    search_strategy = args.search_strategy
    
if args.coordinates:
    start_state = tuple(args.coordinates)
else:
    start_state = (40, 5)
    
if args.num_trial:
    num_trial = args.num_trial
else:
    num_trial = 5
    
if args.maintained_state:
    k = args.maintained_state
else:
    k = 5


def schedule(T):
    return T * 0.95

def test_hill_climbing(title, num_trial=5):
    problem = Problem(img_path)
    best_path = LocalSearchStrategy.random_restart_hill_climbing(problem, num_trial)
    if best_path:
        problem.draw_path(best_path, title)

def test_simulated_annealing_search(title, default_start_state):
    problem = Problem(img_path, state_start=default_start_state)
    best_path = LocalSearchStrategy.simulated_annealing_search(problem, schedule)
    if best_path:
        problem.draw_path(best_path, title)

def test_local_beam_search(title, default_start_state, k=5):
    problem = Problem(img_path, state_start=default_start_state)
    best_path = LocalSearchStrategy.local_beam_search(problem, k)
    if best_path:
        problem.draw_path(best_path, title)
        
if search_strategy.lower() == 'rrhc':
    test_hill_climbing('Random restart hill climbing', num_trial=num_trial)
elif search_strategy.lower() == 'sas':
    test_simulated_annealing_search('Simulated annealing search', default_start_state=start_state)
elif search_strategy.lower() == 'lbs':
    test_local_beam_search('Local beam search', start_state, k=k)
    
