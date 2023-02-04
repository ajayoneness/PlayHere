from rest_framework import serializers
from django.contrib.auth.models import User
from feedback.models import feedback

class testSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class feedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = feedback
        fields = '__all__'