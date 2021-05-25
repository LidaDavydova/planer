from django.urls import path
from . import views
from .views import LoginView, ProfilePage, RegisterView

app_name = 'exel'
 
urlpatterns = [
    path('', views.main, name='main'),
    path('accounts/login/', LoginView.as_view(), name="login"),
    path('accounts/profile/', ProfilePage.as_view(), name="profile"),
    path(r'^accounts/register/$', RegisterView.as_view(), name="register"),
]
