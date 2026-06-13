from django.shortcuts import render , redirect
from .models import Shows
from django.contrib import messages
# Create your views here.
def index(request):
    all_shows = Shows.objects.all()
    context = {"all_shows": all_shows}
    return render(request, "index.html",context)

def new(request):
    context = {
        "old_title": request.session.pop('hold_title', ''),
        "old_network": request.session.pop('hold_network', ''),
        "old_date": request.session.pop('hold_date', ''),
        "old_desc": request.session.pop('hold_desc', ''),
    }
    return render(request, "add_show.html", context)
def create(request):
    if request.method == "POST":
        errors = Shows.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            request.session['hold_title'] = request.POST.get('title', '')
            request.session['hold_network'] = request.POST.get('network', '')
            request.session['hold_date'] = request.POST.get('release_date', '')
            request.session['hold_desc'] = request.POST.get('description', '')
            
            return redirect("/shows/new")
        else:
            Shows.objects.create(title=request.POST["title"], network=request.POST["network"], release_date=request.POST["release_date"], description=request.POST["description"])
    return redirect("/")
def show(request, show_id):
    show = Shows.objects.get(id=show_id)
    context = {"show": show}
    return render(request, "show.html", context)   
def edit(request, show_id):
    show = Shows.objects.get(id=show_id)
    
    context = {
        "show": show,
        "old_title": request.session.pop('edit_hold_title', show.title),
        "old_network": request.session.pop('edit_hold_network', show.network),
        
        "old_date": request.session.pop('edit_hold_date', show.release_date if isinstance(show.release_date, str) else show.release_date.strftime('%Y-%m-%d')),
        "old_desc": request.session.pop('edit_hold_desc', show.description),
    }
    return render(request, "edit_show.html", context)


def update(request, show_id):
    if request.method == "POST":
        errors = Shows.objects.basic_validator(request.POST)
        
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            
            request.session['edit_hold_title'] = request.POST.get('title', '')
            request.session['edit_hold_network'] = request.POST.get('network', '')
            request.session['edit_hold_date'] = request.POST.get('release_date', '')
            request.session['edit_hold_desc'] = request.POST.get('description', '')
            
            return redirect(f"/shows/{show_id}/edit")
            
        else:
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