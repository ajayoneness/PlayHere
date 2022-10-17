from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User,auth

def main(request):
    if request.method == 'POST':
        uname = request.POST['user_name']
        password = request.POST['password']

        user = auth.authenticate(username=uname,password=password)
        print(uname,password)

        if user is not None:
            auth.login(request,user)
            print(user)
            return render(request,"Home.html")
        else:
            print("faild")
            messages.info(request,"invalid user")

    return render(request,'Home.html')
