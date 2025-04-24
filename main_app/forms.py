from django import forms
from .models import Feeding

# ----------------------------
# FeedingForm
# ----------------------------

class FeedingForm(forms.ModelForm):
    # This is a Django ModelForm, which automatically creates form fields
    # based on the Feeding model.

    class Meta:
        model = Feeding  # This form is based on the Feeding model
        fields = ["date", "meal"]  # These are the fields users will fill out in the form

        # Customize the input widget for the 'date' field
        widgets = {
            "date": forms.DateInput(
                format=("%Y-%m-%d"),  # Expected input format (HTML5-compatible)
                attrs={
                    "placeholder": "Select a date",  # Placeholder text for the field
                    "type": "date",  # Uses browser's date picker UI
                },
            ),
        }