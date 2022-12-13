from django.shortcuts import render,HttpResponse
from .models import Book

def index(request):
    return HttpResponse("<h2>Главная</h2>")


def user(request):
    age = request.GET.get("age")
    name = request.GET.get("name")
    return HttpResponse(f"<h2>Имя: {name}  Возраст: {age}</h2>")

def get_info_404(request, question_id):
    return HttpResponse("Такой книги нет, её создавать не нужно")
