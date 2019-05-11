from django.contrib import admin
from django.urls import path
import myapp.views

#path(route, 함수 경로 실행, 경로 이름 짓기)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.home, name="home"),
]