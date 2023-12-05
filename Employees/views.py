from django.shortcuts import render
from .models import *
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import redirect
from .models import EmployeeEducation
from .models import EmployeeExperience



# Create your views here.


def emp_login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['emailid']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        if user:
            login(request,user)
            error = "no"
        else:
            error = "yes"
    return render(request, 'emp_login.html',locals())

def emp_home (request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    return render(request, 'emp_home.html')

def Logout(request):
    logout(request)
    return redirect('index')


def my_experience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    user = request.user
    experience = EmployeeExperience.objects.get(user=user)
    return render(request, 'my_experience.html', locals())


from django.shortcuts import render, redirect
from .models import EmployeeExperience


def edit_myexperience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')

    user = request.user

    try:
        experience = EmployeeExperience.objects.get(user=user)
    except EmployeeExperience.DoesNotExist:
        return redirect('index')
    error = ""
    if request.method == "POST":
        company1name = request.POST.get('company1name')
        company1desig = request.POST.get('company1desig')
        company1salary = request.POST.get('company1salary')
        company1duration = request.POST.get('company1duration')

        company2name = request.POST.get('company2name')
        company2desig = request.POST.get('company2desig')
        company2salary = request.POST.get('compapy2salary')
        company2duration = request.POST.get('company2duration')

        company3name = request.POST.get('company3name')
        company3desig = request.POST.get('company3desig')
        company3salary = request.POST.get('compapy3salary')
        company3duration = request.POST.get('company3duration')


        experience.company1name = company1name
        experience.company1desig = company1desig
        experience.company1salary= company1salary
        experience.company1duration= company1duration

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
        except Exception as e:
            error = str(e)

    return render(request, 'edit_myexperience.html', {'experience': experience, 'error': error})


from django.shortcuts import render, redirect
from .models import EmployeeEducation

def my_education(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    user = request.user
    education = EmployeeEducation.objects.get(user=user)
    return render(request, 'my_education.html', locals())


from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import LeaveRequests, EmployeeExperience, EmployeeEducation, EmployeeDetail

def leave_request(request):
    if not request.user.is_authenticated:
        return redirect('emp_base')

    error = ""
    user = request.user

    try:
        leave = LeaveRequests.objects.get(user=user)
    except LeaveRequests.DoesNotExist:
        # Handle the case where the LeaveRequests object does not exist for the user
        leave = LeaveRequests(user=user)
        leave.save()

    if request.method == "POST":
        sd = request.POST['startdate']
        ed = request.POST['enddate']
        ei = request.POST['empid']
        re_n = request.POST['reason']

        leave.startdate = sd
        leave.enddate = ed
        leave.empid = ei
        leave.reason = re_n

        try:
            leave.save()
            error = "no"
        except Exception as e:
            print(f"Error: {e}")
            error = "yes"

    return render(request, 'leave_request.html', locals())


def leaves(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    leave = LeaveRequests.objects.all()
    return render(request, 'leaves.html', locals())


