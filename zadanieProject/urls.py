from django.contrib import admin
from django.urls import path, include
from .router import router
from rest_framework.authtoken.views import obtain_auth_token
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('auth/', obtain_auth_token),
    path('register/', user_views.register, name='register')


]
