from flask import Flask, flash
from flask import render_template, url_for, redirect, request

app = Flask(__name__)

@app.route("/")
@app.route("/homepage")
def homepage():
    return render_template('homepage.html')

@app.route("/exercise")
def exercise():
    return render_template('exercise.html')

@app.route("/diet")
def diet():
    return render_template('diet.html')

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)