from flask import Flask, render_template, Markup
from constants import Constants
from database import Database
from stats import Stats

app = Flask(Constants.APP_NAME)

@app.route("/", methods=['GET'])
def index():
    # Check table, populate if empty
    # Show two random individuals in the current gen
    return render_template('index.html')

@app.route('/', methods=['POST'])
def decision():
  # Get id of winner and loser
  # Compute elo score change of winner and loser
  # Modify scores in db
  # If we are at the end of current gen, do all the evolution stuff
  # Redirect back to the homepage with 2 new individuals
    pass

@app.route("/history")
def history():
    # Table of generation numbers, params, and elo scores
    # Show images in v2.

    return render_template('history.html')

if __name__ == "__main__":
    app.run(debug=True)
