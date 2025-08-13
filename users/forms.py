from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    """ this is a custom user creation form  where email is required """

    email = forms.EmailField(
        required=True, help_text="We'll never share your email with anyone else."
    )

    class Meta(UserCreationForm.Meta):
        # Add 'email' to the fields tuple here
        fields = UserCreationForm.Meta.fields + ("email",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # style the username field using bootstrap
        self.fields["username"].widget.attrs.update(
            {"class": "form-control w-100", "placeholder": "Enter username"}
        )

        self.fields["email"].widget.attrs.update(
            {
                "class": "form-control w-100",
                "placeholder": "Enter email",
            }
        )

        self.fields["password1"].widget.attrs.update(
            {
                "class": "form-control w-100",
                "placeholder": "Enter password",
            }
        )

        self.fields["password2"].widget.attrs.update(
            {
                "class": "form-control w-100",
                "placeholder": "Enter Confirmation",
            }
        )

    """ handle if password and confirmation is different """

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match. Please try again.")


class CustomLoginForm(AuthenticationForm):
    """ custom class with sytled login form """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields["username"].widget.attrs.update(
            {
                "class": "form-control w-100",
                "placeholder": "Username",
            }
        )
        self.fields["password"].widget.attrs.update(
            {
                "class": "form-control w-100",
                "placeholder": "Password",
            }
        )


class CustomUserChangeForm(UserChangeForm):

    """ custom form for users to edit their credentials """
    password = None

    class Meta(UserChangeForm.Meta):
        model = User
        fields = ["username", "email"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Username"
            }
        )

        self.fields["email"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Email"
            }
        )

       





    