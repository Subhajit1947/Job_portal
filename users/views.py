from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from profiles.models import Profile


def logout_view(request):
    return render(request,'registration/logout.html')

def registerUser(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account/login/')
            
    else:
       form=UserRegistrationForm()
       return render(request,'register.html',{'form':form}) 


