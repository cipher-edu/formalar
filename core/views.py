from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Register
from .forms import *
# Create your views here.
def home (request):
    user = Register.objects.all()
    context =  {
        'user':user
        }
    return render(request, 'index.html', context)

def adduser(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegisterForm()
    context= {
        'form':form 
    }
    return render(request, 'useradd.html',context)