from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class EmailLoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

class StudentIDLoginForm(forms.Form):
    student_id = forms.CharField(max_length=10, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

class StudentIDLoginForm1(forms.Form):
    student_id = forms.CharField(max_length=10, required=True)
    

class PasswordSetupForm(forms.Form):
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password", required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password", required=True)

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

        validate_password(password1)
        return cleaned_data





