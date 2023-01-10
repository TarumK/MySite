from django.shortcuts import render
from django.http import HttpResponse
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

