from django.shortcuts import render , redirect
from .models import Shows
# Create your views here.
def index(request):
    all_shows = Shows.objects.all()
    context = {"all_shows": all_shows}
    return render(request, "index.html",context)

def new(request):
    return render(request, "add_show.html")
def create(request):
    if request.method == "POST":
        Shows.objects.create(title=request.POST["title"], network=request.POST["network"], release_date=request.POST["release_date"], description=request.POST["description"])
    return redirect("/")
def show(request, show_id):
    show = Shows.objects.get(id=show_id)
    context = {"show": show}
    return render(request, "show.html", context)   
def edit(request, show_id):
    show = Shows.objects.get(id=show_id)
    context = {"show": show}
    return render(request, "edit_show.html", context)
def update(request, show_id):
    if request.method == "POST":
        show = Shows.objects.get(id=show_id)
        show.title = request.POST["title"]
        show.network = request.POST["network"]
        show.release_date = request.POST["release_date"]
        show.description = request.POST["description"]
        show.save()
    return redirect("/")
def delete(request, show_id):
    show = Shows.objects.get(id=show_id)
    show.delete()
    return redirect("/")