from flask import Flask, render_template
from app import boxscore
from . import app  # Import Flask application


@app.route("/")
def home():
    return render_template('home.html', 
                        games=boxscore.get_yesterdays_games())