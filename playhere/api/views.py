from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializer import testSerializer,feedbackSerializer,profileSerializer,pointsSerializer,codeajgptSerializer,certificateAPISerializer
from django.contrib.auth.models import User
from feedback.models import feedback
from quiz.models import profile
from points.models import allpoints
from rest_framework.response import Response
from rest_framework.views import APIView
from .helper import Data
from .models import certificateStatic,certificateDynamic



class codeajgptAPI(APIView):
    def post(self, request):
        serializer = codeajgptSerializer(data=request.data)
        if serializer.is_valid():
            input_string = serializer.data.get('input_string')
            api_key = serializer.data.get('api_key')
            no_of_words = serializer.data.get('no_of_words')
            import openai
            openai.api_key = api_key
            completion = openai.Completion.create(engine="text-davinci-003", prompt=input_string, max_tokens=no_of_words)
            output_string = completion.choices[0]['text']
            return Response({'reversed_string': output_string})
        return Response(serializer.errors)


@api_view(['GET'])
def userapi(request):
    obj = User.objects.all()
    serilizer = testSerializer(obj, many=True)
    return Response({
        'status': True,
        "Message": "Success",
        'Data': serilizer.data
    })


@api_view(['GET'])
def feedbackapi(request):
    obj = feedback.objects.all()
    serilizer = feedbackSerializer(obj, many=True)
    return Response({
        'status': True,
        "Message": "Success",
        'Data': serilizer.data
    })


@api_view(['GET'])
def profileapi(request):
    obj = profile.objects.all()
    serilizer = profileSerializer(obj, many=True)
    return Response({
        'status': True,
        "Message": "Success",
        'Data': serilizer.data
    })

@api_view(['GET'])
def pointsapi(request):
    obj = allpoints.objects.all()
    serilizer = pointsSerializer(obj, many=True)
    return Response({
        'status': True,
        "Message": "Success",
        'Data': serilizer.data
    })




class certificateAPI(APIView):

    def post(self, request):
        staticData = certificateStatic.objects.all()[0]
        serializer = certificateAPISerializer(data=request.data)
        if serializer.is_valid():
            user_id = serializer.data.get('user_id')
            name = serializer.data.get('name')
            topic = serializer.data.get('topic')
            exm_date = serializer.data.get('exm_date')


            obj = Data(name, exm_date, topic,staticData.c_name, f"{user_id}.png")

            # obj.imagesize(150, 150, 'playhere.png', 'playherelogo.png')
            t = f'''" is hereby awardes this certificate of achievement for the successfully \n           getting 10,000 rank on 'codeaj.pythonanywhere.com' \n                          by playing {obj.course} on {obj.date} "'''
            obj.imgCreate(staticData.c_bg.path, staticData.c_main_logo.path, 50, obj.name, 34, 177, 76, staticData.c_font_1.path, 320, 200, 250, 70)
            obj.AddText(20, t, 225, 225, 225, staticData.c_font_2.path, 150, 280)
            obj.AddText(15, f'    {staticData.c_ceo_name} \n  CEO of codeaj', 225, 225, 225, staticData.c_font_1.path, 95, 493)
            obj.AddText(15, f'{staticData.c_cto_name} \n  CTO of codeaj', 225, 225, 225, staticData.c_font_1.path, 680, 500)
            obj.AddImage(staticData.c_logo.path, 360, 400)
            # obj.AddImage('cistlogo.jpg',480,450)
            st = f"{obj.outimg} created !!"

            certificateDynamic(user=User.objects.get(id=user_id),name=name,topic=topic,exm_date=exm_date,output_certificate=obj.outimg).save()
            return Response({'status ': st})
            #except:
            #    return Response({'status ':"already created !!!"})


        return Response(serializer.errors)





def test(request):
    return render(request,"newregistation1.html")

