from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout, authenticate
# Create your views here.


def index(request):
    return render(request, 'index.html')


def registration(request):
    error = ""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ei = request.POST['empid']
        em = request.POST['email']
        pwd = request.POST['pwd']
        try:
            user = User.objects.create_user(first_name=fn, last_name=ln, username=em, password=pwd)
            EmployeeDetail.objects.create(user=user, empid=ei)
            EmployeeExperience.objects.create(user=user)
            EmployeeEducation.objects.create(user=user)
            error = "no"
        except:
            error = "yes"
    return render(request, 'registration.html', locals())


def Logout(request):
    logout(request)
    return redirect('index')


def admin_login(request):
    return render(request, 'admin_login.html')


def admin_login(request):
    error = ""
    if request.method == 'POST':
        p = request.POST['username']
        q = request.POST['pwd']
        user = authenticate(username=p, password=q)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, 'admin_login.html', locals())


def admin_changepassword(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')

    error = ""
    user = request.user

    if request.method == "POST":
        current_password = request.POST.get('currentpassword', '')
        new_password = request.POST.get('newpassword', '')

        # Check if the entered current password is correct
        if not user.check_password(current_password):
            error = "not"
        else:
            try:
                # Update the user's password
                user.set_password(new_password)
                user.save()
                error = "no"
            except Exception as e:
                print(e)
                error = "yes"

    return render(request, 'admin_changepassword.html', {'error': error})
