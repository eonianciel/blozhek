from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile


@login_required
def social_dashboard(request):
    return render(request, 'social/social_dashboard.html',
     {'section': 'dashboard'})


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

"""
def register(request):

	if request.method=='POST':
		user_form=UserRegistrationForm(request.POST)
		if user_form.is_valid:
			new_user=user_form.save(commit=False)
			new_user.set_password(user_form.cleaned_data['password'])
			new_user.save()
			Profile.objects.create(user=new_user)

			return render(request, 'social/registration_done.html', {'new_user':new_user})

	else:
		user_form=UserRegistrationForm()
		return render(request, 'social/user_registration.html', {'user_form':user_form})


def edit(request):
	if request.method=='POST':
		user_form=UserEditForm(instance=request.user, data=request.POST)
		profile_form=ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

		if user_form.is_valid and profile_form.is_valid:
			user_form.save()
			profile_form.save()


	else:
		user_form=UserEditForm(instance=request.user)
		profile_form=ProfileEditForm(instance=request.user.profile)

	return render(request, 'social/user_profile_update.html', {'user_form':user_form, 'profile_form':profile_form})

"""
class UserRegistration(View):
    def get(self, request):
        user_form = UserRegistrationForm()
        return render(request, 'social/user_registration.html',
         {'user_form': user_form})

    def post(self, request):
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid:
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            Profile.objects.create(user=new_user)
            new_user.save()
            return render(request, 'social/registration_done.html',
             {'new_user': new_user})


class UpdateUserProfile(View):
    def get(self, request):
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request,'social/user_profile_update.html',
         {'user_form': user_form,'profile_form': profile_form})

    def post(self, request):
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
         data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Профиль успешно изменен')
        else:
            messages.error(request, 'Не удалось изменить профиль')
