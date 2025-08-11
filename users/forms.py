from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="We'll never share your email with anyone else.")

    class Meta(UserCreationForm.Meta):
        # Add 'email' to the fields tuple here
        fields = UserCreationForm.Meta.fields + ('email',)
        
    """ this is a custom user creation form """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # style the username field using bootstrap
        self.fields["username"].widget.attrs.update({
            "class": "form-control w-100", 
            "placeholder": "Enter username"
        })

        self.fields["email"].widget.attrs.update({
            "class": "form-control w-100",
            "placeholder": "Enter email",
        })

        self.fields["password1"].widget.attrs.update({
            "class": "form-control w-100",
            "placeholder": "Enter password",
        })

        self.fields["password2"].widget.attrs.update({
            "class": "form-control w-100",
            "placeholder": "Confirm password",
        })

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match. Please try again.")
