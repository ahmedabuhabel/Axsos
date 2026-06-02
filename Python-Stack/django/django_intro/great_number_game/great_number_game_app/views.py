from django.shortcuts import render, redirect
import random


def home(request):
    # إذا لم يكن هناك رقم عشوائي مخزن في الجلسة، نقوم بتوليده
    if "random_number" not in request.session:
        request.session["random_number"] = random.randint(1, 100)

    # نمرر قيم الـ session الحالية داخل الـ context للوصول إليها في الـ HTML بسهولة
    context = {
        "res": request.session.get("res"),
        "color": request.session.get("color"),
    }
    return render(request, "index.html", context)


def guess(request):
    if request.method == "POST":
        # قراءة التخمين والرقم العشوائي المخزن
        user_guess = int(request.POST.get("guess", 0))
        random_number = request.session.get("random_number")

        if user_guess > random_number:
            request.session["res"] = "Too High!"
            request.session["color"] = "red"
        elif user_guess < random_number:
            request.session["res"] = "Too Low!"
            request.session["color"] = "red"
        else:
            request.session["res"] = f"{random_number} was the number!"
            request.session["color"] = "green"

    return redirect("/")


def reset(request):
    # مسح الجلسة بالكامل لتبدأ اللعبة من جديد برقم عشوائي جديد
    request.session.flush()
    return redirect("/")
