from django.shortcuts import render


def challenge(request):
    return render(request,'chillange.html')

def chquze(request):
    return render(request,'chillangeindex.html')