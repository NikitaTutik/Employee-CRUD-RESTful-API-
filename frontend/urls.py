from django.urls import path
from .views import index, employee_form, employee_delete

urlpatterns = [
    path('', index, name='index'),
    path('employee/<int:id>/', employee_form, name='update'),
    path('employee/delete/<int:id>/', employee_delete, name='delete'),
    path('add/', employee_form, name='insert'),
]
