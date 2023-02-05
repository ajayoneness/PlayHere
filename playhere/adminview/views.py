from django.shortcuts import render

def adminview(request):
    return render(request,'AdminView.html')

def playreview(request):
    return render(request,'playreview.html')
