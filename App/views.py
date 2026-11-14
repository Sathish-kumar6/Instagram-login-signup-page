from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def IndexPage(request):
    return render(request,'./index.html')

def SignUpPage(request):
    return render(request,'./signup.html')

def WelcomePageResponse(request):
    Mobile = request.GET['mobile']
    Password = request.GET['password']
    dob = request.GET['DOB']
    FullName = request.GET['Name']
    UserName = request.GET['User name']

    return render(request,"./welcome.html",context={'name':FullName})
