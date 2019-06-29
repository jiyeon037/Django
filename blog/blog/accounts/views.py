from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth

# 함수를 실행시키기 위한 request가 들어오면 해당 html을 띄워라
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            auth.login(request, user) # 회원가입 후 자동 로그인
            return redirect('blog')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None: # 유저가 존재하는 회원이라면
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST'
        auth.logout(request)
        return redirect('home')
    return render(request, 'login.html')