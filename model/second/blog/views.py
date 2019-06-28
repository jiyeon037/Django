from django.shortcuts import render, get_object_or_404
from .models import Blog # models 파일 안의 Blog import

# 유저에게 보여줄 화면이 단 하나 뿐. 모든 객체에 대한 정보를 뽑아 화면에 출력 가능
def home(request):
    blogs = Blog.objects # 모델로부터 객체 목록(쿼리셋)을 전달받음 # 메소드
    return render(request, 'home.html', {'blogs':blogs})

# 쿼리셋과 메소드의 형식
# 모델.쿼리셋(objects).메소

# 유저에게 보여줄 화면이 몇 번 객체를 인자로 전달받았는지에 따라 달라진다
def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)

    return render(request, 'detail.html', {'blog':blog_detail})