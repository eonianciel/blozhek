from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.contrib.auth.decorators import login_required

from .forms import LoginForm


class UserLogin(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'social/social_login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'],
             password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Авторизация успешна')
                else:
                    return HttpResponse('Аккаунт недоступен')
            else:
                return HttpResponse('Неправильный логин')

@login_required
def social_dashboard(request):
    return render(request, 'social/social_dashboard.html', {'section': 'dashboard'})
