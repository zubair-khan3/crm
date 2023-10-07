from django import forms
from .models import Record


class AddRecord(forms.ModelForm):
   
    first_name  = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First name'}),label='')
    last_name   = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),label='')
    email       = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),label='')
    phone       = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'phone'}),label="")
    city        = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'City'}),label="")
    address     = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),label="")
    zip_code    = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Zipcode'}),label='')

    class Meta:
        model = Record
        fields = ('first_name','last_name','email','phone','city', 'address','zip_code')