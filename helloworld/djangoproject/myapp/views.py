from django.shortcuts import render

# Create your views here.

# request가 들어왔을 때 home.html를 return하는 함수
# 함수 이름은 url 이름과 동일하게 짓는게 좋다
def home(request):
    return render(request, 'home.html')