from django import forms
from django.contrib.auth.models import User



class UserForm(forms.ModelForm):
    name = forms.CharField(max_length=101)
    phone = forms.IntegerField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["name","phone","email","username","password"]
        widgets = {
            "password": forms.widgets.PasswordInput()
        }


 