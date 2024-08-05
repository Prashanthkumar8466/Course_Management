from django.shortcuts import render,redirect
from django.contrib.auth import login ,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Course,enroll_details
def home(request):
    return render(request,'home.html')
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'login successfull')
            return redirect('home')
        else:
           messages.error(request,'please check the details properly')
           return redirect('login')
    return render(request,'User.html')
def admin_login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,"sorry you'r not admin/staff")
                return redirect('login')
        else:
           messages.error(request,'please check password | username')
           return redirect('Admin')
    return render(request,'Admin.html')
def logout_view(request):
    logout(request)
    return redirect('login')
def Register_view(request):
    if request.method =='POST':
        First_Name = request.POST['name']
        Email=request.POST['email']
        username =request.POST['username']
        password =request.POST['password']
        conformation_password =request.POST['cnfrm_password']
        select_user=request.POST['select_user']
        if select_user=='admin':
            select_user=True
        else :
            select_user=False
        if password == conformation_password:
            user = User.objects.filter(username=username)
            if user:
                messages.error(request,'username already exist use different')
                return redirect('register')
            else:
                user=User.objects.create_user(
                    username=username,
                    password=password,
                    email=Email,
                    first_name=First_Name,is_staff=select_user)
                user.save()
                messages.success(request,'created account successfully')
                return redirect('login')
        else:
            messages.error(request,'password should same password twice')
            return redirect('register')
    return render(request,'registration.html')
def user_dash(request):
    courses=Course.objects.all()
    return render(request,'dashboard.html',{'courses':courses})
def add_course(request):
    if request.method=="POST":
        Title=request.POST['course_title']
        Details=request.POST['course_details']
        data=Course.objects.create(Title=Title,Details=Details)
        data.save()
        return redirect('home')
    return render(request,'addcourse.html')
def enroll_course(request,pk):
    course=Course.objects.get(id=pk)
    exist=enroll_details.objects.filter(user=request.user,course=course)
    if exist:
        return redirect('dashboard')
    else:
        data=enroll_details.objects.create(user=request.user,course=course)
        data.save()
    return redirect('dashboard')
def enrolled_course(request):
    all=enroll_details.objects.all()
    data=enroll_details.objects.filter(user=request.user)
    return render(request,'enrolled_list.html',{'data':data,'all':all})
def course_View(request):
    data=Course.objects.all()
    return render(request,'delete_course.html',{'data':data})
def course_delete(request,pk):
    data=Course.objects.get(id=pk)
    data.delete()
    return redirect('viewcourse')
def manage_user(request):
    data=User.objects.all()
    return render(request,'userlist.html',{'data':data})
#update