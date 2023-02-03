from django.shortcuts import render


def addquestions(request):
    return render(request,'addquestion.html')