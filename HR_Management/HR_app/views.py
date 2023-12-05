from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout, authenticate
# Create your views here.



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


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request, 'admin_home.html')


def all_employee(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    employee = EmployeeDetail.objects.all()
    return render(request, 'all_employee.html', locals())


def delete_employee(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    user = User.objects.get(id=pid)
    user.delete()
    return redirect('all_employee')

def edit_profile(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    employee = EmployeeDetail.objects.get(id=pid)
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
    return render(request, 'edit_profile.html', locals())


def edit_education(request, pid):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = User.objects.get(id=pid)
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
    return render(request, 'edit_education.html', locals())


def edit_experience(request, pid):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = User.objects.get(id=pid)
    experience = EmployeeExperience.objects.get(user=user)
    if request.method == "POST":
        company1name = request.POST['company1name']
        company1desig = request.POST['company1desig']
        company1salary = request.POST['company1salary']
        company1duration = request.POST['company1duration']

        company2name = request.POST['company2name']
        company2desig = request.POST['company2desig']
        company2salary = request.POST['company2salary']
        company2duration = request.POST['company2duration']

        company3name = request.POST['company3name']
        company3desig = request.POST['company3desig']
        company3salary = request.POST['company3salary']
        company3duration = request.POST['company3duration']

        experience.company1name = company1name
        experience.company1desig = company1desig
        experience.company1salary = company1salary
        experience.company1duration = company1duration

        experience.company2name = company2name
        experience.company2desig = company2desig
        experience.company2salary = company2salary
        experience.company2duration = company2duration

        experience.company3name = company3name
        experience.company3desig = company3desig
        experience.company3salary = company3salary
        experience.company3duration = company3duration

        try:
            experience.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'edit_experience.html', locals())

