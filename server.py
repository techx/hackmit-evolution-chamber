from flask import Flask, render_template
from constants import Constants
from database import get_db

app = Flask(__name__)

@app.route("/")
@app.route("/<text>")
def index(text=Constants.generation_length):
    return render_template('index.html', text=text)

if __name__ == "__main__":
    app.run()
