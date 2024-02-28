from django.urls import include, path

# import routers
from rest_framework import routers 
# import everything from views
from .views import *
  
# define the router
router = routers.DefaultRouter()
router.register(r'movie', MovieViewSet)
router.register(r'student', StudentViewSet)


# 1st method - Through admin pannel.

# 2nd method- through command line(py manage.py drf_create_token <user_nam>)

# 3rd method- By exposing an api endpoint.
# for using this install pip install httpie
from rest_framework.authtoken.views import obtain_auth_token 
# specify URL Path for rest_framework
urlpatterns = [
    path('', include(router.urls)),
    path("gettoken/", obtain_auth_token), # 3rd method to generate token
]

# hit thin in new terminal http POST http://127.0.0.1:8000/gettoken/ username="admin" password="admin"