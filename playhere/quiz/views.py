from django.shortcuts import render,redirect
from .models import profile,cat,questions
import random

lis = []
def profile1(request):
    lis.clear()
    rank = 0
    pobj = profile.objects.filter(p_username=request.user.username).order_by("-id")
    code = profile.objects.filter(category = 'coding' , p_username=request.user.username).count()
    com = profile.objects.filter(category='communication', p_username=request.user.username).count()
    apti = profile.objects.filter(category='aptitude', p_username=request.user.username).count()
    # Total Rank
    for i in pobj:
        rank += i.score

    request.session['rank'] = rank

    try:
        obj = pobj[0]
    except:
        obj =0

    mostplayed = {'coding':code,'communication':com,'aptitude':apti}
    if mostplayed['coding'] == 0 or mostplayed['communication'] == 0 or mostplayed['aptitude'] == 0 :
        mosplay = 0
    else:
        mosplay = max(mostplayed, key=mostplayed.get)

    return render(request,'profile.html',{'pobj':obj,"pobjcount":pobj.count(),'mostplay':mosplay,'rank':rank})


def cate(request):
    lis.clear()
    catobj = cat.objects.all()

    if request.method == 'POST':
        c_val = request.POST['catbtn']
        request.session['category'] = c_val

        total_cat = questions.objects.filter(category=request.session['category'])
        count = total_cat.count() - 1
        if count > 0:
            q_number = random.randint(0, count)
        else:
            q_number = random.randint(0, 0)

        return redirect(f'/quiz/ques/{q_number}')

    return render(request,'category.html',{'category':catobj})



def ques(request,idd):
    R1=random.randint(20,200)
    R2 = random.randint(20,200)
    G1 = random.randint(20, 200)
    G2 = random.randint(20, 200)
    B1 = random.randint(20, 200)
    B2 = random.randint(20, 200)

    if 'category' in request.session :
        total_cat = questions.objects.filter(category=request.session['category'])
        count = total_cat.count()-1
        try:
            q_number = idd
            qn = total_cat[q_number]
        except:
            qn=''

    if request.method == 'POST':
        try:
            ti = request.POST['tim']
            print("time : ", ti)
            select = request.POST['o']
        except:
            select =''
        print(select)
        if select != '':
            if int(total_cat[q_number].answer) == int(select):
                lis.append(1)
                print('correct answer')
                if len(lis) >= 10:
                    sumlis = sum(lis)
                    print(sumlis)
                    lis.clear()
                    return redirect(f'/quiz/result/{sumlis}')

                return redirect(f'/quiz/ques/{random.randint(0,count)}')

            else:
                lis.append(0)
                print('incorrect Answer')
                if len(lis) >= 10:
                    sumlis = sum(lis)
                    print(sumlis)
                    lis.clear()
                    return redirect(f'/quiz/result/{sumlis}')

                return redirect(f'/quiz/ques/{random.randint(0, count)}')


        else :
            pass

    dis = {'r1': R1, 'r2': R2, 'g1': G1, 'g2': G2, 'b1': B1, 'b2': B2, 'q_obj': qn,'count':len(lis)+1}

    return render(request,'index.html',dis)


def result(request,slis):
    try:
        emoji = {
            0: [
                'https://media3.giphy.com/media/IzcFv6WJ4310bDeGjo/giphy.gif?cid=ecf05e47k3nntc4i6h0dka9ewtqldv1j67d5m52kurajmtj1&rid=giphy.gif&ct=g',
                'you need to practice more '],
            1:['https://media3.giphy.com/media/IzcFv6WJ4310bDeGjo/giphy.gif?cid=ecf05e47k3nntc4i6h0dka9ewtqldv1j67d5m52kurajmtj1&rid=giphy.gif&ct=g','you need to practice more '],
            2:['https://media0.giphy.com/media/h4OGa0npayrJX2NRPT/giphy.gif?cid=ecf05e47k3nntc4i6h0dka9ewtqldv1j67d5m52kurajmtj1&rid=giphy.gif&ct=g','ohh so sad'],
            3:['https://media0.giphy.com/media/kfS15Gnvf9UhkwafJn/giphy.gif?cid=ecf05e47la8y34pgr207jtpmr6k5q9q7g34sr6zm25oywgoe&rid=giphy.gif&ct=g','not bad'],
            4:['https://media2.giphy.com/media/j4l0mCdcTFRyY4Bc5s/giphy.gif?cid=ecf05e47la8y34pgr207jtpmr6k5q9q7g34sr6zm25oywgoe&rid=giphy.gif&ct=g','nice'],
            5:['https://media0.giphy.com/media/USUIWSteF8DJoc5Snd/giphy.gif?cid=ecf05e47xzour2hglinyz1ann7ex8ghg5tgw5i31et1sym2h&rid=giphy.gif&ct=g','not bad'],
            6:['https://media4.giphy.com/media/hp3dmEypS0FaoyzWLR/giphy.gif?cid=ecf05e47xzour2hglinyz1ann7ex8ghg5tgw5i31et1sym2h&rid=giphy.gif&ct=g','wow'],
            7:['https://media1.giphy.com/media/hVlZnRT6QW1DeYj6We/giphy.gif?cid=ecf05e47xzour2hglinyz1ann7ex8ghg5tgw5i31et1sym2h&rid=giphy.gif&ct=g','suer'],
            8:['https://media4.giphy.com/media/UQDSBzfyiBKvgFcSTw/giphy.gif?cid=ecf05e47xzour2hglinyz1ann7ex8ghg5tgw5i31et1sym2h&rid=giphy.gif&ct=g','good'],
            9:['https://media2.giphy.com/media/LOnt6uqjD9OexmQJRB/giphy.gif?cid=ecf05e47xzour2hglinyz1ann7ex8ghg5tgw5i31et1sym2h&rid=giphy.gif&ct=g','sweet'],
            10:['https://media3.giphy.com/media/lRXY41yFFi9RfNXyPN/giphy.gif?cid=ecf05e47mxr383ar6o6yxhzr5iaoa8j6iw17z3axmyc3dgau&rid=giphy.gif&ct=g','so, sweet'],
            }
        ucategory = request.session['category']
        uscore = slis
        emo = emoji[uscore]
        #comming soon
        utimetaken = 0

        if request.user.is_authenticated :
            uname = request.user.username

            save_user_data = profile(p_username=uname, category=ucategory, score=uscore, timetkaen=utimetaken )
            save_user_data.save()

        return render(request,'result.html',{'score':uscore,'emoji':emo})
    except:
         return redirect('/')




def certificate(request):

    return render(request,'certification.html',{'rank' : request.session['rank']})
