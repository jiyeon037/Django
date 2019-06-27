from django.contrib import admin
from .models import Blog # 같은 폴더 안 models 안에서 Blog 객체를 가져와라

admin.site.register(Blog) # admin 사이트에 등록

# Register your models here.
