from allauth.account.forms import ChangePasswordForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from .forms import UpdateEmailForm, UpdateNameForm


def home(request):
    return render(request, "core/home.html")


@require_POST
def echo(request):
    message = request.POST.get("message", "")
    return HttpResponse(f"Echo: {message}")


@login_required
def profile(request):
    name_form = UpdateNameForm(request.POST or None, instance=request.user)
    email_form = UpdateEmailForm(request.POST or None, instance=request.user)
    password_form = ChangePasswordForm(user=request.user, data=request.POST or None)

    if request.method == "POST":
        if "email" in request.POST and email_form.is_valid():
            email_form.save()
        elif "oldpassword" in request.POST and password_form.is_valid():
            password_form.save()
        elif "first_name" or "last_name" in request.POST and name_form.is_valid():
            name_form.save()
        return redirect("profile")
    return render(
        request,
        "core/profile.html",
        {
            "email_form": email_form,
            "password_form": password_form,
            "name_form": name_form,
        },
    )
