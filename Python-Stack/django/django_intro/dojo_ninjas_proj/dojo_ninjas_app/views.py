from django.shortcuts import render, redirect
from .models import Dojos, Ninjas


def index(request):
    context = {"all_dojos": Dojos.objects.all()}
    return render(request, "index.html", context)


def create_dojo(request):
    if request.method == "POST":
        Dojos.objects.create(
            name=request.POST["name"],
            city=request.POST["city"],
            state=request.POST["state"],
        )
    return redirect("/")


def create_ninja(request):
    if request.method == "POST":
        dojo_instance = Dojos.objects.get(id=request.POST["dojo_id"])

        Ninjas.objects.create(
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            dojo=dojo_instance,
        )
    return redirect("/")


def delete_dojo(request, dojo_id):
    if request.method == "POST":
        dojo_to_delete = Dojos.objects.get(id=dojo_id)
        dojo_to_delete.delete()
    return redirect("/")
