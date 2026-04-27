from flask import Flask, render_template

app = Flask(__name__)


# Passing num and color as parameters
@app.route("/play/<num>/<color>")
def hello_world(num=3, color="blue"):
    num = int(num)
    return render_template("index.html", count=num, color=color)


if __name__ == "__main__":
    app.run(debug=True)
