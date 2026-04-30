from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():

    print(request.form)
    name_from_form = request.form["name"]
    location_from_form = request.form["location"]
    favorite_language_from_form = request.form["favorite_language"]
    comment_from_form = request.form["comment"]
    return render_template(
        "result.html",
        name=name_from_form,
        location=location_from_form,
        favorite_language=favorite_language_from_form,
        comment=comment_from_form,
    )


if __name__ == "__main__":
    app.run(debug=True)
