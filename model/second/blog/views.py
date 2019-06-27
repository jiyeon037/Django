from django.shortcuts import render
from .models import Blog # models 파일 안의 Blog import

def home(request):
    blogs = Blog.objects # 모델로부터 객체 목록(쿼리셋)을 전달받음 # 메소드
    return render(request, 'home.html', {'blogs':blogs})

# 쿼리셋과 메소드의 형식
# 모델.쿼리셋(objects).메소
