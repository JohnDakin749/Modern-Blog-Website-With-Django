from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib import messages
from. import forms

def signup_view(request):
    if request.method =='POST':
        form = forms.CreateUser(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('articles:list')
    else:
        form = forms.CreateUser()
    return render(request,'accounts/signup_views.html',{'form':form})


def login_view(request):
    if request.method =='POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

def logout_view(request):
    if request.method =='POST':
        logout(request)
        return redirect('articles:list')
    
    
def changePassword(request):
    if request.method =='POST':
        form = forms.changePasswordForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your password has been updated successfully")
            return redirect('articles:list')
    else:
        form = forms.changePasswordForm(user=request.user)
    return render(request,'accounts/changePassword.html',{'form':form})

def resetPassword(request):
    if request.method =='POST':
        form = forms.resetPassword(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.resetPassword()        
    return render(request,'accounts/resetPassword.html',{'form':form})