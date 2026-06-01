from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse


# Create your views here.
def root_method(request):
    return redirect("/blogs/")


def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")


def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")


def create(request):
    return redirect("/blogs/")


def show(request, number):
    return HttpResponse(f"placeholder to display blog {number}")


def edit(request, number):
    return HttpResponse(f"placeholder to edit blog {number}")


def destroy(request, number):
    return redirect("/blogs/")


def response(request):
    return JsonResponse(
        {
            "title": "My First Blog Post",
            "content": "This is the content of the blog post placeholder.",
        }
    )
