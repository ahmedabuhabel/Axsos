from django.shortcuts import render, redirect
from .models import Users


def index(request):
    all_users = Users.objects.all()
    context = {"users": all_users}
    return render(request, "index.html", context)


def create(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        age = request.POST.get("age")

        Users.objects.create(
            first_name=first_name, last_name=last_name, email=email, age=age
        )

    return redirect("/")
