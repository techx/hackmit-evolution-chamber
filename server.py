from flask import Flask, render_template
from constants import Constants
from database import get_db
from stats import Stats

app = Flask(Constants.APP_NAME)

@app.route("/")
@app.route("/<text>")
def index(text=Constants.generation_length):
    Stats.increment()
    return render_template('index.html', text=Stats.num())

if __name__ == "__main__":
    app.run()
