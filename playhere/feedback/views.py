from django.shortcuts import render,redirect
from .models import feedback

def feed(request):
    if request.user.username != "":
        fbobj = feedback.objects.filter(uname=request.user.username).order_by("-id")
        print(fbobj)
        try:
            yourobj = fbobj[0]
            yourfeed = fbobj[0].mes
            print(f"hi {request.user.username} your feed is {yourfeed}")
            if request.method == 'POST':
                uname = request.user.username
                userproblem = request.POST['userproblem']

                if userproblem != "":
                    feedback.objects.filter(uname=request.user.username).update(mes=userproblem)
                    print("message update to db")
                else:
                    feedback.objects.filter(uname=request.user.username).delete()
                return redirect('/feedback/')

        except:
            yourobj = ""
            yourfeed = ""
            print("no feed")
            if request.method == 'POST':
                uname = request.user.username
                userproblem = request.POST['userproblem']

                if userproblem != "":
                    fb = feedback(uname=uname, mes=userproblem)
                    fb.save()
                    print("save to db")
                else:
                    feedback.objects.filter(uname=request.user.username).delete()
                return redirect('/feedback/')



        fobj = feedback.objects.all().order_by("-id")
        return render(request,'feedback.html',{'fb':fobj,"yourfeed":yourfeed,"yourobj":yourobj})
    else:
        return redirect("/")