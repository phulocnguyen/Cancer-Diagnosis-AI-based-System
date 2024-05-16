
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

class RegisterForm(forms.ModelForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={"placeholder": "Enter email-address", "class": "form-control"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter username", "class": "form-control"}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"placeholder": "Enter password", "class": "form-control"}))
    
    class Meta:
        model = get_user_model()
        fields = ["email", "username", "password"]
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user