from django.shortcuts import render
from quiz.models import profile

def points(request):
    print(request.user)
    profileObj = profile.objects.filter(p_username=request.user).order_by("-id")
    return render(request,'points.html',{'profileobj': profileObj})