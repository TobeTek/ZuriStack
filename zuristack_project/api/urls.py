from django.urls import path 

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

app_name = 'api'

router = DefaultRouter()

router.register('users', views.UserViewSet, basename='user')

urlpatterns = router.urls 

urlpatterns += [
    path('token/', obtain_auth_token, name='get_token'),
]