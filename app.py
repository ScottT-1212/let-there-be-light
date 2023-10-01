from cs50 import SQL
from flask import Flask, render_template, request, redirect, url_for, flash, session
import csv


# configure application
app = Flask(__name__)

# configure cs50 to allow sqlite3 functionality
db = SQL("sqlite:///leaderboard.db")

# Configure session
app.secret_key = "Let there be light"

# read list of level data from csv
levels = []

with open("levels.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["status"] == "active":
            row["number"] = int(row["number"])
            levels.append(row)


# give a session variable to all templates
@app.context_processor
def inject_session_status():
    return dict(session_active="user" in session)


@app.route("/", methods=["GET", "POST"])
def index():
    if "user" in session:
        # put list of levels into level selection box
        return render_template("index.html", levels=levels)

    return render_template("index.html")


@app.route("/practice", methods=["GET"])
def practice():
    return render_template("practice.html")


@app.route("/game", methods=["GET", "POST"])
def game():
    if "user" in session:
        # submit score to leaderboard using post method
        if request.method == "POST":
            score = request.form.get("score")
            level_number = int(request.form.get("level_number"))

            db.execute(
                "INSERT INTO leaderboard (player_name, level_number, score, grid_size) VALUES (?, ?, ?, ?);",
                session["user"],
                level_number,
                score,
                3,
            )

            flash("Score submitted to leaderboard")

            return redirect(url_for("index"))

        # redirect invalid level numbers
        try:
            level_number = int(request.args.get("level"))
            if level_number < 1 or level_number > len(levels):
                flash("Please select a valid level number")
                return redirect(url_for("index"))
        except ValueError:
            flash("Please select a valid level number")
            return redirect(url_for("index"))

        # load selected level
        index = level_number - 1

        return render_template("game.html", levels=levels[index])

    else:
        return redirect(url_for("login"))


@app.route("/leaderboard", methods=["GET", "POST"])
def leaderboard():
    if request.method == "POST":
        # reject invalid level numbers
        try:
            level_number = int(request.form.get("level"))
            if level_number < 1 or level_number > len(levels):
                flash("Select a valid level")
                return redirect(url_for("leaderboard"))
        except ValueError:
            flash("Select a valid level")
            return redirect(url_for("leaderboard"))

        # retrieve data from database
        leaderboard = db.execute(
            "SELECT * FROM leaderboard WHERE level_number = ? ORDER BY score ASC LIMIT 10;",
            level_number,
        )

        return render_template(
            "leaderboard.html", levels=levels, leaderboard=leaderboard
        )

    return render_template("leaderboard.html", levels=levels)


@app.route("/login", methods=["GET", "POST"])
def login():
    # either begin or end the user's session
    if request.method == "POST":
        user = request.form.get("username")
        session["user"] = user
        flash("Logged in as " + session["user"])

        return redirect(url_for("index"))

    # display login/logout page depending on whether the user is logged in
    if "user" in session:
        return redirect(url_for("logout"))

    return render_template("login.html")


@app.route("/logout", methods=["GET", "POST"])
def logout():
    if request.method == "POST":
        del session["user"]
        flash("You have logged out")

        return redirect(url_for("login"))

    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("logout.html", user=session["user"])
