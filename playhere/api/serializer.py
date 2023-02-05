from rest_framework import serializers
from django.contrib.auth.models import User
from feedback.models import feedback
from quiz.models import profile
from points.models import allpoints



class testSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class feedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = feedback
        fields = '__all__'


class profileSerializer(serializers.ModelSerializer):

    class Meta:
        model = profile
        fields = '__all__'

class pointsSerializer(serializers.ModelSerializer):

    class Meta:
        model = allpoints
        fields = '__all__'
