from django.urls import path
# from rest_framework.authtoken.views import ObtainAuthToken

from . import views

urlpatterns = [
    path('registration/', views.RegistrationApiView.as_view(), name='registration'),
    path('token/login/', views.CustomObtainAuthToken.as_view(), name='token-login')
]
