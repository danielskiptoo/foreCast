from django.contrib import admin
from django.contrib.auth import views as auth
from django.urls import path, include

import main.views
import accounts.views



urlpatterns = [

    path('',main.views.IndexView, name='index'),

    path('login/', accounts.views.SignInView.as_view(), name='login'),
    path('logout/', auth.LogoutView.as_view(template_name='index.html'), name='logout'),

    path('register/', accounts.views.SignUpView.as_view(), name='register'),
    path('activate/<code>/', accounts.views.ActivateView.as_view(), name='activate'),

    path('password/change/', auth.PasswordChangeView.as_view(
        template_name='accounts/password_change_form.html'), name='password_change'),
    path('password/change/done/', auth.PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html'), name='password_change_done'),

    path('password/reset/', auth.PasswordResetView.as_view(template_name='accounts/password_reset.html'),
         name='password_reset'),
    path('password/reset/done/', auth.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'), name='password_reset_done'),

    path('password/<uidb64>/<token>/',
         auth.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password/reset/done/',
         auth.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),

   # path('^oauth/', include('social_django.urls', namespace='social')),
]
(r'^logout/$', 'django.contrib.auth.views.logout',
                          {'next_page': '/successfully_logged_out/'})