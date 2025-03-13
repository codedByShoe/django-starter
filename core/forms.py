from django import forms
from django.contrib.auth import get_user_model
from allauth.account.forms import SignupForm
from unfold import widgets


class UpdateEmailForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ["email"]
        widgets = {"email": forms.EmailInput()}


class UpdateNameForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name"]
        widgets = {"first_name": forms.TextInput(), "last_name": forms.TextInput()}


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label="First Name")
    last_name = forms.CharField(max_length=30, label="Last Name")

    def save(self, request):
        user = super().save(request)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.save()
        return user
