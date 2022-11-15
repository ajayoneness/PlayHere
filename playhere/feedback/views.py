from django.shortcuts import render,redirect
from .models import feedback

def feed(request):
    if request.method == 'POST':
        uname = request.user.username
        userproblem = request.POST['userproblem']

        fb = feedback(uname=uname,mes=userproblem)
        fb.save()
        print("save to db")

        return redirect('/feedback/')

    fobj = feedback.objects.all().order_by("-id")
    return render(request,'feedback.html',{'fb':fobj})