from django import forms
from django.contrib.auth.models import User

class Registration(forms.Form):

    first_name= forms.CharField(max_length=255,widget= forms.TextInput(attrs={'class': 'form-control','placeholder': 'First Name' }))
    last_name= forms.CharField(max_length=255,widget= forms.TextInput(attrs={'class': 'form-control','placeholder': 'Last Name' }))
    email= forms.EmailField(widget= forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email' }))
    username= forms.CharField(widget= forms.TextInput(attrs={'class': 'form-control' ,'placeholder': 'Username'}))
    password= forms.CharField(widget= forms.PasswordInput(attrs={'class': 'form-control' ,'placeholder': 'Password'}))
    confirm_password= forms.CharField(widget= forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Confirm Password' }))


    def clean(self):
        x= super().clean()

        if x['password'] != x['confirm_password']:
            raise forms.ValidationError('Password Not Match')
            
        if User.objects.filter(email= x['email']).exists():
            raise forms.ValidationError("Email already exists")
        
        if User.objects.filter(username= x['username']).exists():
            raise forms.ValidationError("Username already exists")
        
        

        


