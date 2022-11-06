from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User,auth

def main(request):
    if request.method == 'POST':
        uname = request.POST['user_name']
        password = request.POST['password']
        text = request.POST['hsec']


        user = auth.authenticate(username=uname,password=password)

        if user is not None:
            auth.login(request,user)
            return render(request,"Home.html")
        else:
            messages.info(request,"invalid user")


    return render(request,'Home.html')
