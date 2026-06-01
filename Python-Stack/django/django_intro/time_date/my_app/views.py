from django.shortcuts import render
from time import localtime, strftime


def index(request):
    context = {
        "date": strftime("%b %d, %Y", localtime()),
        "time": strftime("%I:%M %p", localtime()),
    }
    return render(request, "index.html", context)
