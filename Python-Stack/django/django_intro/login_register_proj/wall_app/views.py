from django.shortcuts import render, redirect
from django.contrib import messages
from login_register_app.models import User
from .models import Message, Comment

def wall_index(request):
    if 'user_id' not in request.session:
        return redirect("/")
        
    context = {
        "current_user": User.objects.get(id=request.session['user_id']),
        "all_messages": Message.objects.all().order_by('-created_at') 
    }
    return render(request, "wall.html", context)

def post_message(request):
    if request.method == "POST":
        errors = Message.objects.message_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            user_obj = User.objects.get(id=request.session['user_id'])
            Message.objects.create(
                message=request.POST['message'],
                user=user_obj
            )
    return redirect("/wall")

def post_comment(request, message_id):
    if request.method == "POST":
        errors = Comment.objects.comment_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            user_obj = User.objects.get(id=request.session['user_id'])
            msg_obj = Message.objects.get(id=message_id)
            Comment.objects.create(
                comment=request.POST['comment'],
                user=user_obj,
                message=msg_obj
            )
    return redirect("/wall")

def delete_message(request, message_id):
    if request.method == "POST":
        message_to_delete = Message.objects.get(id=message_id)
        
        if message_to_delete.user.id == request.session['user_id']:
            
            if message_to_delete.can_be_deleted():
                message_to_delete.delete()
                messages.success(request, "Message deleted successfully.")
            else:
                messages.error(request, "Action expired! Messages can only be deleted within 30 minutes.")
        else:
            messages.error(request, "Unauthorized action!")
            
    return redirect("/wall")