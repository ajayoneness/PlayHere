from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.shortcuts import render,HttpResponse,redirect

def register(request):
    if request.method == "POST":
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        uname = (request.POST['user_name']).lower()
        email = (request.POST['email']).lower()
        pass1 = request.POST['password']
        pass2 = request.POST['repassword']


        if pass1==pass2:
            if User.objects.filter(username=uname).exists():
                messages.info(request,'Username Taken')

            elif User.objects.filter(email = email).exists():
                messages.info(request,'Email Already Taken')

            else:
                user=User.objects.create_user(username=uname,password=pass1,email=email,first_name = fname,last_name = lname)
                user.save()
                return redirect('/#login')
        else:
            messages.info(request, 'both password are not save')

    return render(request,"newregistation.html")


# def login(request):
#     if request.method == 'POST':
#         uname = request.POST['user_name']
#         password = request.POST['password']
#
#         user = auth.authenticate(username=uname,password=password)
#         print(user)
#
#         if user is not None:
#             auth.login(request,user)
#             return render(request,"Home.html")
#         else:
#             messages.info(request,"invalid user")
#
#     return render(request,"Home.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
