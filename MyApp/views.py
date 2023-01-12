from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from .forms import UserForm
# Create your views here.


def index(request):
    return HttpResponse('Добро пожаловать в моё приложение!')


def about(request, name, age):
    return HttpResponse(f'''<h1>О пользователе</h1>
                    <hr>
                    <p>Имя: {name}
                    <p>Возраст: {age}
                        ''')


def contact(request):
    return HttpResponse('<H1>Контакты</H1>')


def info(request):
    host = request.META['HTTP_HOST']
    browser = request.META['HTTP_USER_AGENT']
    path = request.path
    return HttpResponse(f'{host} <p>{browser} <p> {path}')


def form(request):
    name = ['Murat', 'Beslan', 'Peter']
    data = {'name': name}
    user_form = UserForm()
    return render(request, 'index.html', {"form": user_form})

def e403(request):
    return HttpResponseForbidden()

