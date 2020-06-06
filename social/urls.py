from django.urls import path
from django.contrib import admin
from django.contrib.auth import views

from .views import*

urlpatterns = [
    path('login/', UserLogin.as_view(), name='social_login'),
    path('dashboard/', social_dashboard, name='social_dashboard'),
    path('socials/login/', views.LoginView.as_view(), name='login'),
    path('socials/logout/', views.LogoutView.as_view(next_page='/'),
     name='logout'),
    path('password_change/', views.PasswordChangeView.as_view(),
     name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(),
     name='password_change_done'),
    path('password_reset/', views.PasswordResetView.as_view(),
     name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(),
     name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(),
     name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(),
     name='password_reset_complete'),
    #path('', include('django.contrib.auth.urls')),
    path('registration/', UserRegistration.as_view(), name='user_registration'),
    path('update/', UpdateUserProfile.as_view(), name='update_user_profile'),
    #path('registration/', register, name='user_registration'),
    #path('update/', edit, name='update_user_profile'),
]
