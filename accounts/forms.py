from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm,PasswordResetForm
from django.contrib.auth.models import User

class CreateUser(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']
        
        
class changePasswordForm(PasswordChangeForm):
    pass


class resetPassword(PasswordResetForm):
    pass