from flask import Flask, render_template
from constants import Constants
from database import get_db

app = Flask(__name__)

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


@app.route("/history")
def history():
	# Table of generation numbers, params, and elo scores
	# Show images in v2.

	return render_template('history.html')

@app.route("/<text>")
def index(text=Constants.generation_length):
    return render_template('index.html', text=text)

if __name__ == "__main__":
    app.run()
