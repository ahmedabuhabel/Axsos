from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "index.html", rows=8, columns=8, color1="black", color2="white"
    )


@app.route("/<int:columns>")
def cols(columns):
    return render_template(
        "index.html", rows=8, columns=columns, color1="black", color2="white"
    )


@app.route("/<int:rows>/<int:columns>")
def rows(rows, columns):
    return render_template(
        "index.html", rows=rows, columns=columns, color1="black", color2="white"
    )


@app.route("/<int:rows>/<int:columns>/<color1>/<color2>")
def index(rows, columns, color1, color2):
    return render_template(
        "index.html", rows=rows, columns=columns, color1=color1, color2=color2
    )


def no_response():
    return "No response"


@app.errorhandler(404)
def page_not_found(e):
    return no_response(), 404


if __name__ == "__main__":
    app.run(debug=True)
