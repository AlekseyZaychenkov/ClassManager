from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from account.forms import CuratorAuthenticationForm, CuratorUpdateForm
from django.urls import reverse_lazy

from manager.models import Curator


def login_view(request):
    context = dict()
    context["email_does_not_exist"] = False
    context["password_is_wrong"] = False

    if 'action' in request.POST and request.POST['action'] == 'go_to_login':
        form = CuratorAuthenticationForm(request.POST)
    elif 'email' in request.POST and request.POST:
        context["email"] = request.POST['email']
        email = request.POST['email']
        password = request.POST['password']
        form = CuratorAuthenticationForm(request.POST)

        if not Curator.objects.filter(email=email).exists():
            context["email_does_not_exist"] = True
        elif not authenticate(email=email, password=password):
            context["password_is_wrong"] = True
        else:
            if form.is_valid():
                user = authenticate(email=email, password=password)
                login(request, user)
                return redirect('home')
    else:
        form = CuratorAuthenticationForm()

    context['form'] = form

    return render(request, "login.html", context)


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def profile(request):
    context = dict()

    context['email'] = request.user.email
    context['nick_name'] = request.user.nick_name

    context['date_joined'] = request.user.date_joined
    context['is_admin'] = request.user.is_admin
    context['is_staff'] = request.user.is_staff
    context['is_superuser'] = request.user.is_superuser

    return render(request, "profile.html", context)


@login_required
def edit_profile(request):
    context = dict()
    user = Curator.objects.get(email=request.user.email)

    if request.POST and request.POST['action'] == 'save_profile':
        form = CuratorUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CuratorUpdateForm(initial={'email': request.user.email,
                                          'nick_name': request.user.nick_name})
    context['form'] = form

    return render(request, "edit_profile.html", context)


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('profile')
