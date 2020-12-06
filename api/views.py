from rest_framework import viewsets
from .serializers import UserSerializer, EmployeeSerializer
from .models import Employee
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated


class UserViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )

    queryset = User.objects.all()
    serializer_class = UserSerializer


class EmployeeViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
