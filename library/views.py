from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView



def home_page(request):
    return render(request, 'home_page.html', {'title': 'Главная страница'})


class Register_user(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'

class Login(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

