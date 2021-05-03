from django.shortcuts import render,redirect
from .models import User,Lawyer,Client
from django.contrib.auth.models import auth
# Create your views here.


def registerLawyer(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        RUA = request.POST['RUA']

        user = User.objects.create_user(username=user_name,first_name=first_name,last_name=last_name,email=email,password=password)
        user.is_lawyer = True
        user.save()
        lawyer = Lawyer.objects.create(user=user,RUA=RUA)
        lawyer.save()
        return  redirect('/')
    else:
        return render(request, 'LawyerRegister.html')

def registerClient(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username=user_name, first_name=first_name, last_name=last_name, email=email,password=password)
        user.is_client = True
        user.save()
        client = Client.objects.create(user=user)
        client.save()
        return redirect('/')
    else:
        return render(request, 'ClientRegister.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            return redirect('login')
    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')