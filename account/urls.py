from django.urls import path
from account.views import logout_view, login_view, profile, edit_profile, ChangePasswordView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', login_view, name="login"),
    path('logout', logout_view, name="logout"),


    path('account/password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
         name='password_change_done'),

    path('account/password_change/',
         auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
         name='password_change'),

    path('account/password_reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),

    path('account/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('account/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    path('account/reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),

    path('account/profile/', profile, name="profile"),

    path('account/edit_profile/', edit_profile, name="edit_profile"),

    path('account/change_password/', ChangePasswordView.as_view(), name='change_password'),
]
