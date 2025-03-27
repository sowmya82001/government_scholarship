from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Application  # Import the custom User model

class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['statement']
        widgets = {
            'statement': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
