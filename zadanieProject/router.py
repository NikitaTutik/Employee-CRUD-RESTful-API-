from api.views import EmployeeViewset, UserViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register('employee', EmployeeViewset)
router.register('users', UserViewset)

