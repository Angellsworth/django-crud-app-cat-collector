from django import forms
from .models import Feeding
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# ----------------------------
# FeedingForm
# ----------------------------

class FeedingForm(forms.ModelForm):
    class Meta:
        model = Feeding
        fields = ["date", "meal"]
        widgets = {
            "date": forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={
                    "placeholder": "Select a date",
                    "type": "date",
                },
            ),
        }

# ----------------------------
# CustomUserCreationForm
# ----------------------------


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Simplify or remove help text for cleaner UI
        self.fields['username'].widget.attrs.update({'placeholder': 'Choose a username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Your email'})
        self.fields['first_name'].widget.attrs.update({'placeholder': 'First name'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Last name'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Create a password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm password'})