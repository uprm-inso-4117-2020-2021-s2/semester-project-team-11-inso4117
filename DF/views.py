from django.shortcuts import render
from accounts.models import Lawyer,Client,User

# Create your views here.
def index(request):
    return render(request, 'index.html')

def form(request):
    return render(request,'form.html')

def search(request):
    context = True
    return render(request,"search.html",context=context)

