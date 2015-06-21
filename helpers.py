import species
import genetic
from constants import *

def populate_current_generation_if_empty():
    raise NotImplementedError()

def get_random_parameterss(num=2):
    # returns list of tuples (id, parameters)
    raise NotImplementedError()

def render_parameters(parameters):
    return species.generate(parameters)

def modify_scores(winner_id, loser_id):
    raise NotImplementedError()

def end_of_generation():
    raise NotImplementedError()

def save_best_to_history():
    raise NotImplementedError()

def kill_unfit():
    raise NotImplementedError()

def breed():
    raise NotImplementedError()

def reset_scores():
    raise NotImplementedError()

def end_generation():
    if not end_of_generation():
        return
    save_best_to_history()
    kill_unfit()
    breed()
    reset_scores()

def history():
    # return list of tuples (generation number, params, scores)
    raise NotImplementedError()
