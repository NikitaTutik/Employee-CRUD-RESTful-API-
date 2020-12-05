from rest_framework import viewsets
from .serializers import UserSerializer, EmployeeSerializer
from .models import Employee
from django.contrib.auth.models import User


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer