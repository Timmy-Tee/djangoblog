from django import forms
from .models import Profile

class UserProfile(forms.ModelForm):
     password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control mt-2 mb-2'}))
     password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class': 'form-control mt-2 mb-2'}))
     class Meta:
          model = Profile
          exclude = 'user',
          fields = ['username', 'email','password1', 'password2', 'userImage']
          widgets = {
               'username': forms.TextInput(attrs={'class': 'form-control mt-2 mb-2'}),
               'email': forms.EmailInput(attrs={'class': 'form-control mt-2 mb-2'}),
               'userImage': forms.FileInput(attrs={'class': 'form-control mt-2 mb-2'}),
          }