from django.shortcuts import render, redirect
import random
from datetime import datetime


def index(request):
    if "gold" not in request.session:
        request.session["gold"] = 0
    if "activities" not in request.session:
        request.session["activities"] = []

    context = {
        "gold": request.session["gold"],
        "activities": request.session["activities"],
    }
    return render(request, "index.html", context)


def process_money(request, location):
    if request.method == "POST":
        gold_earned = 0
        style_class = "text-success"

        if location == "farm":
            gold_earned = random.randint(10, 20)
        elif location == "cave":
            gold_earned = random.randint(10, 20)
        elif location == "house":
            gold_earned = random.randint(10, 20)
        elif location == "quest":
            gold_earned = random.randint(-50, 50)
            if gold_earned < 0:
                style_class = "text-danger"

        request.session["gold"] += gold_earned

        timestamp = datetime.now().strftime("%Y/%m/%d %I:%M %p")
        if gold_earned >= 0:
            activity_text = (
                f"Earned {gold_earned} golds from the {location}! ({timestamp})"
            )
        else:
            activity_text = f"Entered a casino and lost {abs(gold_earned)} golds from the quest... Ouch. ({timestamp})"

        current_activities = request.session["activities"]
        current_activities.insert(0, {"text": activity_text, "class": style_class})
        request.session["activities"] = current_activities

    return redirect("/")


def reset(request):
    request.session.flush()
    return redirect("/")
