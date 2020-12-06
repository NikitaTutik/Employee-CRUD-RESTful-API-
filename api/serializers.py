from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Employee
from rest_framework.authtoken.models import Token


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        Token.objects.create(user=user)
        return user


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


