from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from .models import Portfolio

# Create your views here.
def home(request):
    blogs = Blog.objects #쿼리셋
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, blog_id):
    # 몇번 객체인지 받아주는 함수는 get_object_or_404(class, 검색조건)
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details':details})

def new(request): # new.html 띄워주는 함수
    return render(request, 'new.html')

def create(request): # 입력받은 내용을 데이터베이스에 넣어주는 함수
    blog = Blog() # Blog 클래스로부터 blog라는 객체 생성
    blog.title = request.GET['title'] # html form에서 입력한 내용들을 객체 안 변수들에게 갖고와줌
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save() # 객체에 저장한 내용들을 DB에 저장
    # 객체.delete() // db에서 지워라
    return redirect('/blog/' + str(blog.id))

    # render함수와 redirect함수의 차이
    # redirect : 인자로 url을 받음, 프로젝트 외 url 연결 가능
    # render : python 함수 안에서 수행한 내용을 html 상에서 전달하기 위해 세번째 인자로 키값을 받음

def portfolio(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio.html', {'portfolios':portfolios})