from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializer import testSerializer,feedbackSerializer,profileSerializer,pointsSerializer,codeajgptSerializer
from django.contrib.auth.models import User
from feedback.models import feedback
from quiz.models import profile
from points.models import allpoints
from rest_framework.response import Response
from rest_framework.views import APIView



class codeajgptAPI(APIView):
    def post(self, request):
        serializer = codeajgptSerializer(data=request.data)
        if serializer.is_valid():
            input_string = serializer.data.get('input_string')
            import openai
            openai.api_key = "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"
            completion = openai.Completion.create(engine="text-davinci-003", prompt=input_string, max_tokens=1000)
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


def test(request):
    return render(request,"newregistation1.html")

