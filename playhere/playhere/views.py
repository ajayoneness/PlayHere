from django.shortcuts import render,redirect
from django.contrib import messages
from quiz.models import addmore
from django.contrib.auth.models import User,auth

def main(request):
    request.session['lis'] = 0
    request.session['tlis'] = 0
    request.session['count'] = 1
    request.session['countt'] = 0
    request.session['tenque'] = {}
    if request.method == 'POST':
        uname = (request.POST['user_name']).lower()
        password = request.POST['password']
        text = request.POST['hsec']

        if '.com' in uname and '@' in uname:
            try:
                uname = User.objects.get(email=uname).username
            except:
                messages.info(request, "This Email is not registered")
                return redirect("/#login")

        user = auth.authenticate(username=uname,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/quiz/")
        else:
            messages.info(request,"invalid user")
            return redirect("/#login")

    try:
        aobj = addmore.objects.filter(user=request.user).order_by("-id")
        print(aobj[0].profile_picture)

    except:
        aobj = "ajay"
        print(aobj)

    return render(request,'Home.html',{"aobj":aobj})
