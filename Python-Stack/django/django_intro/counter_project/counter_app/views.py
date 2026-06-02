from django.shortcuts import render, redirect


def home(request):
    if "visits" in request.session:
        request.session["visits"] += 1
    else:
        request.session["visits"] = 0

    if "count" in request.session:
        request.session["count"] += 1
    else:
        request.session["count"] = 0

    context = {"count": request.session["count"], "visits": request.session["visits"]}
    return render(request, "index.html", context)


def incrementByTwo(request):
    request.session["count"] += 1
    return redirect("/")


def byAmount(request):
    if request.method == "POST":
        amount = int(request.POST.get("amount", 1))
        request.session["count"] += amount - 1
    return redirect("/")


def reset(request):
    request.session["count"] = -1
    return redirect("/")


def destroy_session(request):
    request.session.flush()
    return redirect("/")
