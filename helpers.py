import species
import genetic
from constants import *
from database import Database
import elo


'''
A series of...
functions that do who know what
'''

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
        newIndividualParameters = genetic.random_individual_parameters()
        Database.add_individual_to_current_generation(newIndividualParameters)

def render_individual(parameters):
    return species.generate(parameters)

def modify_scores(winner_id, loser_id):
    winnerIndividual = Database.get_individual_for_id(winner_id)
    loserIndividual = Database.get_individual_for_id(loser_id)

    (newWinnerScore, newLoserScore) = elo.get_elos_for_result(winnerIndividual["elo"], loserIndividual["elo"], elo.ResultType.WIN)

    Database.update_elo_for_id(winner_id, newWinnerScore)
    Database.update_elo_for_id(loser_id, newLoserScore)
    Database.incr_comparisons()

def end_of_generation():
    '''
    Returns bool whether it is the end of a generation
    '''
    return Database.num_comparisons() >= Constants.COMPARISONS_PER_GENERATION

def save_best_to_history():
    sorted_individuals = Database.get_all_individuals_sorted()

    Database.add_historical_individual(sorted_individuals[0])

def kill_unfit():
    sorted_individuals = Database.get_all_individuals_sorted()
    unfit = sorted_individuals[-Constants.KILL_SIZE:]
    Database.delete_individuals(unfit)

def breed():
    alive_number = Constants.POPULATION_SIZE - Constants.KILL_SIZE
    sorted_individuals = Database.get_all_individuals_sorted()[:alive_number]
    for i in range(alive_number):
        pick1, pick2 = random.sample(sorted_individuals, 2)
        parameters = genetic.combine_and_mutate(pick1, pick2)
        Database.add_individual_to_current_generation(parameters)

def reset_scores():
    for individual in Database.get_all_individuals_sorted():
        Database.update_elo_for_id(individual["id"],1000.0)

def end_generation():
    if not end_of_generation():
        return
    Database.reset_comparisons()
    save_best_to_history()
    kill_unfit()
    breed()
    reset_scores()

def history():
    return Database.get_historical_individuals()
