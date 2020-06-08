from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from .models import Question
from .forms import LoginForm, SignUpForm
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView

from .controller import main

DEFAULT_ROBOT_NAME = 'Roboko'

def indexfunc(request):
    user = Question.objects.get(id=request.user.id)

    if request.method == 'POST':
        user.favorite_food = request.POST['favorite_food']
        user.save()

    return render(request, 'main_app/index.html')
