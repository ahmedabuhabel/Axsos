from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():

    return "Hello World!"


def no_response():
    return "No response"


@app.errorhandler(404)
def page_not_found(e):
    return no_response(), 404


@app.route("/champion")
def champion():
    return "Champion!"


@app.route("/say/<name>")
def say(name):
    return f"Hi {name}!"


@app.route("/repeat/<int:num>/<name>")
def repeat(num, name):
    print(num, name)
    return f"{name} " * num


if __name__ == "__main__":
    app.run(debug=True)
