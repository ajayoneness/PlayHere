from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import testSerializer,feedbackSerializer
from django.contrib.auth.models import User
from feedback.models import feedback



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


def test(request):
    return render(request,"newregistation1.html")

