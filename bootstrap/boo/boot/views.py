from django.shortcuts import render
import boot

def home(request):
    return render(request, 'hello.html')