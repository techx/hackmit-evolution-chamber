import species
import random

def combine_and_mutate(parent_a, parent_b):
    new = species.mutate(species.combine(parent_a, parent_b))
    assert is_valid(new)
    return new

def random_individual_parameters():
    parameters = {}
    domains = species.domains()
    for param in domains:
        parameters[param] = random.choice(domains[param])
    return parameters

# check if all parameters are in domain
def is_valid(parameters):
    return True # yolo
    domains = species.domains()
    covered = set()
    for param in parameters:
        covered.add(param)
        value = parameters[param]
        if value not in domains[param]:
            return False
    return covered == set(domains.keys())

def combine_random(parent_a, parent_b):
    new = {}
    for param in parent_a:
        new[param] = random.choice([parent_a, parent_b])[param]
    return new
