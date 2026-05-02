#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)


@app.route("/")
def index():

    return render_template("index.html")


@app.route("/checkout", methods=["POST"])
def checkout():
    print(request.form)
    strawberry = request.form["strawberry"]
    raspberry = request.form["raspberry"]
    apple = request.form["apple"]
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    student_id = request.form["student_id"]
    return render_template(
        "checkout.html",
        strawberry=strawberry,
        raspberry=raspberry,
        apple=apple,
        first_name=first_name,
        last_name=last_name,
        student_id=student_id,
    )


@app.route("/fruits")
def fruits():
    basedir = os.path.abspath(os.path.dirname(__file__))
    img_dir = os.path.join(basedir, "static", "img")
    fruits_list_images = os.listdir(img_dir)
    return render_template("fruits.html", images=fruits_list_images)


if __name__ == "__main__":
    app.run(debug=True)
