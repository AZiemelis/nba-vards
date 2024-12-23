from flask import Flask, render_template
import boxscore

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html', 
                           games=boxscore.get_yesterdays_games())