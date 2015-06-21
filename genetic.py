import species

def combine_and_mutate(parent_a, parent_b):
    new = species.mutate(species.combine(parent_a, parent_b))
    assert is_valid(new)
    return new

# check if all paramemters are in domain
def is_valid(individual):
    raise NotImplementedError()
