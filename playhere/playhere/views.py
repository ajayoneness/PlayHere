from django.shortcuts import render
from django.contrib import messages
from quiz.models import addmore
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

    try:
        aobj = addmore.objects.filter(user=request.user).order_by("-id")
        print(aobj[0].profile_picture)

    except:
        aobj = "ajay"
        print(aobj)

    return render(request,'Home.html',{"aobj":aobj})
