from django.shortcuts import render

def adminview(request):
    return render(request,'AdminView.html')