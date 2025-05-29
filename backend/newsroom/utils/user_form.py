from django import forms


class UserForm(forms.Form):
    first_name = forms.CharField(required=True, strip=True)
    last_name = forms.CharField(required=True, strip=True)
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
