from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'), # accounts/signup/
    path('login/', views.login, name='login'), # blogproject의 urls.py에서 설정해둠
    path('logout/', views.logout, name='logout'),
]