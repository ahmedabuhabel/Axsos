from django.shortcuts import render, redirect


def index(request):
    return render(request, "index.html")


def result(request):
    if request.method == "POST":
        context = {
            "name": request.POST.get("name"),
            "location": request.POST.get("location"),
            "favorite_language": request.POST.get("favorite_language"),
            "comment": request.POST.get("comment"),
        }
        return render(request, "result.html", context)

    return redirect("/")
