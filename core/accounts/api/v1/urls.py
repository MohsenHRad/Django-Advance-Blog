from django.urls import path

from . import views

urlpatterns = [
    path('registration/', views.RegistrationApiView.as_view(), name='registration')
]
