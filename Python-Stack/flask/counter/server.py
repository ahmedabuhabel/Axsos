from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"


@app.route("/")
def home():
    if "visits" in session:
        session["visits"] += 1
    else:
        session["visits"] = 0
    if "count" in session:
        session["count"] += 1
    else:
        session["count"] = 0
    return render_template(
        "index.html", count=session["count"], visits=session["visits"]
    )


@app.route("/incrementByTwo")
def incrementByTwo():
    session["count"] += 1
    return redirect("/")


@app.route("/byAmount", methods=["POST"])
def byAmount():
    session["count"] += int(request.form["amount"] - 1)
    return redirect("/")


@app.route("/reset")
def reset():
    session["count"] = -1
    return redirect("/")


@app.route("/destroy_session")
def destroy_session():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
