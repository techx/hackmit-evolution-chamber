from flask import Flask, render_template, Markup, request
from constants import Constants
from database import Database
from helpers import *
from elo import *

app = Flask(Constants.APP_NAME)

@app.route("/", methods=['GET'])
def index():
    # Check table, populate if empty
    # Show two random individuals in the current gen
    populate_current_generation_if_empty()
    a, b = Database.get_random_individuals(2)
    ar = render_individual(a['parameters'])
    br = render_individual(b['parameters'])
    aid, bid = a['id'], b['id']
    prg = str(float(Database.num_comparisons()) / Constants.COMPARISONS_PER_GENERATION * 100)
    gen = len(Database.get_historical_individuals())

    return render_template('index.html', left_id=aid, left=ar, right_id=bid, right=br, progress=prg, generation=gen)

@app.route('/', methods=['POST'])
def decision():
    # Get id of winner and loser
    # Compute elo score change of winner and loser
    # Modify scores in db
    # If we are at the end of current gen, do all the evolution stuff
    # Redirect back to the homepage with 2 new individuals
    form = request.form
    generation = int(request.form['generation'])
    if generation != len(Database.get_historical_individuals()):
        return 'ignored'
    winner_id = request.form['winner'] # string
    loser_id = request.form['loser'] # string

    modify_scores(winner_id, loser_id)
    save_decision(winner_id, loser_id)
    end_generation()

    return 'ok'


@app.route("/history")
def history():
    # Table of generation numbers, params, and elo scores
    # Show images in v2.

    history_of_gens = get_history()
    for i in history_of_gens:
        i['render'] = render_individual(i['parameters'])

    return render_template('history.html', history_of_gens=history_of_gens)

if __name__ == "__main__":
    app.run(debug=True)
