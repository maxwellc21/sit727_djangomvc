from django.shortcuts import render
from django.http import JsonResponse
from .models import Message

def home(request):
    return render(request, 'djangomvc_app/index.html')

def get_message(request):
    message = Message.get_default_message()
    return JsonResponse({'message': message.content})