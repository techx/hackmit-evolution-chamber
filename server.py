from flask import Flask, render_template, Markup
from constants import Constants
from database import get_db
from stats import Stats
from helpers import *
from elo import *

app = Flask(Constants.APP_NAME)

@app.route("/", methods=['GET'])
def index():
    # Check table, populate if empty
    # Show two random individuals in the current gen
    populate_current_generation_if_empty()
    species_to_compare = render_individuals(get_random_individuals())

    return render_template('index.html', species=species_to_compare)

@app.route('/', methods=['POST'])
def decision():
  # Get id of winner and loser
  # Compute elo score change of winner and loser
  # Modify scores in db
  # If we are at the end of current gen, do all the evolution stuff
  # Redirect back to the homepage with 2 new individuals
    winner_id = 1 # TODO
    loser_id = 2

    modify_scores(winner_id, loser_id)
    end_generation()

    #TODO: redirect to index 


@app.route("/history")
def history():
    # Table of generation numbers, params, and elo scores
    # Show images in v2.

    history_of_gens = history()

    return render_template('history.html', history_of_gens=history_of_gens)

if __name__ == "__main__":
    app.run(debug=True)
