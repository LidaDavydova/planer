from django.urls import path
from . import views
from .views import *

app_name = 'exel'
 
urlpatterns = [
    path('', views.main, name='main'),
    path('prepare/', Prepare_calc.as_view(), name='prepare'),
    path('accounts/login/', LoginView.as_view(), name="login"),
    path('accounts/profile/', ProfilePage.as_view(), name="profile"),
    path('accounts/register/', RegisterView.as_view(), name="register"),
    #path('prepare/calculate/', views.calculate, name='calculate'),
    path('prepare/calculate/', Calc.as_view(), name='calculate'),
    path('download_calc', Download_calc.as_view(), name='download_calc'),
]

