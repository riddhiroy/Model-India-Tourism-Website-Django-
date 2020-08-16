from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User
# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if (request.method=='POST'):
        username=request.POST['username']
        password=request.POST['password']
        user= auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid username or password')
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def register(request):
    if(request.method == 'POST'):
        first=request.POST['firstname']
        last=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if User.objects.filter(username=username).exists():
            messages.info(request,'username already there')
            return render(request,'register.html') 
        elif User.objects.filter(email=email).exists():
            messages.info(request,'email already there')
            return render(request,'register.html') 
        elif password1!=password2:
            messages.info(request,'password not matching')
            return render(request,'register.html')
        else:
            user =User.objects.create_user(username=username,password=password1,email=email, first_name=first, last_name= last )
            user.save()
            return redirect('/')

    else:
        return render(request,'register.html')