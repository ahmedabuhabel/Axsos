from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt 

def index(request):
    if 'user_id' in request.session:
        return redirect("/success")
    
    context = {
        "reg_first_name": request.session.pop('hold_reg_first_name', ''),
        "reg_last_name": request.session.pop('hold_reg_last_name', ''),
        "reg_email": request.session.pop('hold_reg_email', ''),
        "reg_birthday": request.session.pop('hold_reg_birthday', ''),
        "login_email": request.session.pop('hold_login_email', ''),
    }
    return render(request, "index.html", context)

def register(request):
    if request.method == "POST":
        errors = User.objects.register_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            request.session['hold_reg_first_name'] = request.POST.get('first_name', '')
            request.session['hold_reg_last_name'] = request.POST.get('last_name', '')
            request.session['hold_reg_email'] = request.POST.get('email', '')
            request.session['hold_reg_birthday'] = request.POST.get('birthday', '')
            
            return redirect("/")
        else:
            hash_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            new_user = User.objects.create(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                birthday=request.POST['birthday'],
                password=hash_pw
            )
            request.session['user_id'] = new_user.id
            return redirect("/success")
    return redirect("/")

def login(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                
            request.session['hold_login_email'] = request.POST.get('email', '')
            return redirect("/")
            
        user_list = User.objects.filter(email=request.POST['email'])
        if user_list.exists():
            logged_user = user_list[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['user_id'] = logged_user.id
                return redirect("/success")
        
        request.session['hold_login_email'] = request.POST.get('email', '')
        messages.error(request, "Invalid Email or Password.")
    return redirect("/")

def success(request):
    if 'user_id' not in request.session:
        return redirect("/")
        
    context = {
        "current_user": User.objects.get(id=request.session['user_id'])
    }
    return render(request, "success.html", context)

def logout(request):
    request.session.flush()
    return redirect("/")