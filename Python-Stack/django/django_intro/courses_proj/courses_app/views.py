from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course, Description, Comment

def index(request):
    context = {
        "all_courses": Course.objects.all().order_by('-created_at'), 
        "hold_name": request.session.pop('hold_course_name', ''),
        "hold_desc": request.session.pop('hold_course_desc', ''),
    }
    return render(request, "index.html", context)

def create_course(request):
    if request.method == "POST":
        errors = Course.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            request.session['hold_course_name'] = request.POST.get('name', '')
            request.session['hold_course_desc'] = request.POST.get('description', '')
            return redirect("/")
        
        desc_obj = Description.objects.create(content=request.POST['description'])
        
        Course.objects.create(
            name=request.POST['name'],
            description=desc_obj
        )
    return redirect("/")

def confirm_delete(request, course_id):
    context = {
        "course": Course.objects.get(id=course_id)
    }
    return render(request, "confirm.html", context)

def delete_course(request, course_id):
    if request.method == "POST":
        course = Course.objects.get(id=course_id)
        course.delete() 
    return redirect("/")

def course_comments(request, course_id):
    course_obj = Course.objects.get(id=course_id)
    if request.method == "POST":
        comment_content = request.POST.get('comment', '').strip()
        if len(comment_content) > 0:
            Comment.objects.create(content=comment_content, course=course_obj)
        return redirect(f"/courses/{course_id}/comments")
        
    context = {
        "course": course_obj,
        "comments": course_obj.comments.all()
    }
    return render(request, "comments.html", context)