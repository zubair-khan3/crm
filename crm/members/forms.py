from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name  = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email      = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    


    class Meta:
        model  = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            #'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            #'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            #'email' : forms.EmailField(attrs={'class':'form-control'}),
            #'password1' : forms.PasswordInput(attrs={'class':'form-control'}),
            #'password2' : forms.PasswordInput(attrs={'class':'form-control'}),
        } 