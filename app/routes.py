from flask import Flask, render_template
from app import boxscore
from . import app  # Import Flask application
from prometheus_flask_exporter import PrometheusMetrics

metrics = PrometheusMetrics(app)
@app.route('/metrics')
def metrics():
    return metrics.handler()


@app.route("/")
def home():
    return render_template('home.html', 
                        games=boxscore.get_yesterdays_games())