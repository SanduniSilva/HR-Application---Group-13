from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout, authenticate
# Create your views here.


def index(request):
    return render(request, 'index.html')


def Logout(request):
    logout(request)
    return redirect('index')


def profile(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    employee = EmployeeDetail.objects.get(user=user)
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ei = request.POST['empid']
        dept = request.POST['department']
        designation = request.POST['designation']
        contact = request.POST['contact']
        jdte = request.POST['jdate']
        gender = request.POST['gender']

        employee.user.first_name = fn
        employee.user.last_name = ln
        employee.empid = ei
        employee.empdept = dept
        employee.designation = designation
        employee.contact = contact
        employee.gender = gender

        if jdte:
            employee.joiningdate = jdte

        try:
            employee.save()
            employee.user.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'profile.html', locals())


def edit_myeducation(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    education = EmployeeEducation.objects.get(user=user)
    if request.method == "POST":
        coursepg = request.POST['coursepg']
        universitypg = request.POST['universitypg']
        pgraduationyr = request.POST['pgraduationyr']
        percentagepg = request.POST['percentagepg']

        coursegra = request.POST['coursegra']
        universitygra = request.POST['universitygra']
        graduationyr = request.POST['graduationyr']
        percentagegr = request.POST['percentagegr']

        coursessc = request.POST['coursessc']
        universityssc = request.POST['universityssc']
        graduationyrssc = request.POST['graduationyrssc']
        percentagessc = request.POST['percentagessc']

        coursehsc = request.POST['coursehsc']
        universityhsc = request.POST['universityhsc']
        graduationyrhsc = request.POST['graduationyrhsc']
        percentagehsc = request.POST['percentagehsc']

        education.coursepg = coursepg
        education.universitypg = universitypg
        education.graduationyr = graduationyr
        education.percentagepg = percentagepg

        education.coursegra = coursegra
        education.universitygra = universitygra
        education.graduationyr = graduationyr
        education.percentagegr = percentagegr

        education.coursessc = coursessc
        education.universityssc= universityssc
        education.graduationyrssc = graduationyrssc
        education.percentagessc = percentagessc

        education.coursehsc = coursehsc
        education.universityhsc = universityhsc
        education.graduationyrhsc = graduationyrhsc
        education.percentagehsc = percentagehsc

        try:
            education.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'edit_myeducation.html', locals())


def change_password(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')

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

    return render(request, 'change_password.html', {'error': error})



