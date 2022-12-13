from django.shortcuts import render
from .models import fullresult
from quiz.models import questions

def full_result(request):

    fres = request.session['tenque']
    qus = questions.objects.filter(category=request.session['category'])

    time = request.session['ttime']
    ucategory = request.session['category']
    score = request.session['uscore']
    points = ((score * 100) - (time)) / 100


    dic =[]
    for i in range(1,11):
        dic.append([qus[fres[f"q{i}"]].question,qus[fres[f"q{i}"]].subquestion,qus[fres[f"q{i}"]].option1,qus[fres[f"q{i}"]].option2,qus[fres[f"q{i}"]].option3,qus[fres[f"q{i}"]].option4,qus[fres[f"q{i}"]].answer,qus[fres[f"q{i}"]].category,qus[fres[f"q{i}"]].topic,fres[f"ya{i}"]])

    return render(request,'fullresult.html',{'qus':qus,'data':dic,'time':time,'ucat':ucategory,'score':score,'points':points})