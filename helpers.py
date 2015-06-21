import species as species
import genetic
from constants import *
from database import Database
import elo as elo


'''
Individual, as retrieved from the database
A dictionary with fields:
"elo"
"id"
"parameters" : dictionary
'''

def populate_current_generation_if_empty():
    if not Database.current_generation_is_empty():
        return
    print "Adding new random individuals to generation."
    for i in xrange(0, Constants.POPULATION_SIZE):
        newIndividual = species.random_individual()
        Database.add_individual_to_current_generation(newIndividual)

def get_random_parameterss(num=2):
    # returns list of tuples (id, parameters)
    raise NotImplementedError()

def render_parameters(parameters):
    # note that an individual != 'parameters'
    return species.generate(parameters)

def modify_scores(winner_id, loser_id):
    winnerIndividual = Database.get_individual_for_id(winner_id)
    loserIndividual = Database.get_individual_for_id(loser_id)

    (newWinnerScore, newLoserScore) = elo.get_elos_for_result(winnerIndividual["elo"], loserIndividual["elo"], elo.ResultType.WIN)

    Database.update_elo_for_id(winner_id, newWinnerScore)
    Database.update_elo_for_id(loser_id, newLoserScore)
    # TODO need to incrememnt the number of comparisons in the database somewhere. I don't think it belongs in here.

''' 
Returns bool whether it is the end of a generation
'''
def end_of_generation():
    return Database.num_comparisons() >= Constants.COMPARISONS_PER_GENERATION

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
