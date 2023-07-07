from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import History


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'

        
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields=['id','username','first_name','email']