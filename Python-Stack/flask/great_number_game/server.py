from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)
app.secret_key = "secret"


@app.route("/")
def home():
    if "random_number" not in session:
        session["random_number"] = random.randint(1, 100)
    return render_template("index.html")


@app.route("/guess", methods=["POST"])
def guess():

    guess = int(request.form["guess"])
    random_number = session["random_number"]

    if guess > random_number:
        session["res"] = "Too High!"
        session["color"] = "red"
    elif guess < random_number:
        session["res"] = "Too Low!"
        session["color"] = "red"
    else:
        session["res"] = f"{random_number} was the number!"
        session["color"] = "green"

    return redirect("/")


@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
