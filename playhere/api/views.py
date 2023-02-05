from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import testSerializer,feedbackSerializer,profileSerializer,pointsSerializer
from django.contrib.auth.models import User
from feedback.models import feedback
from quiz.models import profile
from points.models import allpoints


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

