##
# elo.py
# provides implementation of ELO algorithm to determine
# change in fitness given a malicious act of nature.
##


K_FACTOR = 50 # weighting factor. The larger the more significant a match
# ^ in chess it's usually 15-16 for grandmasters and 32 for weak players
BETA = 400

class ResultType:
    WIN = 1
    LOSE = 2
    DRAW = 3

'''
Returns a tuple (newELOYou, newELOThem)
example usage:
(2100NewElo, 2000NewElo) = get_elos_for_result(2100, 2000, ResultType.LOSE)
'''
def get_elos_for_result(eloYou, eloOpponent, result):
    # get expected values
    expectedYou = 1. / (1.+10.**(float(eloOpponent - eloYou)/BETA))
    expectedThem = 1 - expectedYou # 1. / (1+10**((eloYou - eloOpponent)/BETA))

    # actual scores
    if result == ResultType.WIN:
        actualYou = 1
    elif result == ResultType.LOSE:
        actualYou = 0
    else:
        actualYou = 0.5
    actualThem = 1. - actualYou

    newELOYou = eloYou + K_FACTOR * (actualYou - expectedYou)
    newELOOpponent = eloOpponent + K_FACTOR * (actualThem - expectedThem)
    return (newELOYou, newELOOpponent)


'''
Test to make sure elo calculated correctly given constants
'''
def test_elos():
    def eloTuplesEqual(tupleA, tupleB):
        return abs(tupleA[0] - tupleB[0]) <= 1 and abs(tupleA[1] - tupleB[1]) <= 1
    assert eloTuplesEqual(get_elos_for_result(1200, 1200, ResultType.DRAW), (1200, 1200))
    assert eloTuplesEqual(get_elos_for_result(800, 1400, ResultType.DRAW), (823, 1377))
    assert eloTuplesEqual(get_elos_for_result(200, 2000, ResultType.WIN), (249, 1951))
    assert eloTuplesEqual(get_elos_for_result(2100, 2000, ResultType.WIN), (2117, 1983))
    assert eloTuplesEqual(get_elos_for_result(2100, 2000, ResultType.LOSE), (2067, 2033))
    print "tests pass"


#test_elos()