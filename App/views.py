from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth.models import User


def loginpage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(request , username=username,password=password)

        if user is not None:
            print('username is valid')
            login(request,user,backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')        
        else :
            messages.info(request,"username or password is incorrect")
    return render(request,'login.html')

def signuppage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    context = {'form':form}
    return render(request,'signup.html',context=context)

# @login_required
def homepage(request):
    users = User.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        for i in users:
            if i.username == username:
                print('matchfound')
                messages.error(request,"Username taken ")
                break
        else:
            print('no match found')
            messages.success(request,"Username available")
    
    return render(request , 'homepage.html')

def logoutpage(request):

    logout(request)

    return redirect('login')
