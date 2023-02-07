from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, Select, FileInput

from .models import UserProfile


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30,label= 'User Name :')
    email = forms.EmailField(max_length=200,label= 'Email :')
    first_name = forms.CharField(max_length=100,label= 'First Name :')
    last_name = forms.CharField(max_length=100,label= 'Last Name :')

    class Meta:
        model = User
        fields = ('username', 'email','first_name','last_name', 'password1', 'password2', )
        widgets = {
            'username'  : TextInput(attrs={'class': 'sizefull s-text7 p-l-22 p-r-22','placeholder':'Nombre de Usuarios'}),
            'email'     : EmailInput(attrs={'class': 'sizefull s-text7 p-l-22 p-r-22','placeholder':'Email'}),
            'first_name': TextInput(attrs={'class': 'sizefull s-text7 p-l-22 p-r-22','placeholder':'Nombre'}),
            'last_name' : TextInput(attrs={'class': 'sizefull s-text7 p-l-22 p-r-22','placeholder':'Apellido' }),
        }

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ( 'username','email','first_name','last_name')
        widgets = {
            'username'  : TextInput(attrs={'class': 's-text7 size16 p-l-23 p-r-50','placeholder':'Nombre de Usuarios'}),
            'email'     : EmailInput(attrs={'class': 's-text7 size16 p-l-23 p-r-50','placeholder':'Email'}),
            'first_name': TextInput(attrs={'class': 's-text7 size16 p-l-23 p-r-50','placeholder':'Nombre'}),
            'last_name' : TextInput(attrs={'class': 's-text7 size16 p-l-23 p-r-50','placeholder':'Apellido' }),
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'address', 'city','image')
        widgets = {
            'phone'     : TextInput(attrs={'class': 's-text7 size16 p-l-23 p-r-50','placeholder':'Telefono'}),
            'address'   : TextInput(attrs={'class': 's-text7 size16 p-l-23 p-r-50','placeholder':'Dirrecion'}),
            'city'   : TextInput(attrs={'class': 's-text7 size16 p-l-23 p-r-50','placeholder':'Pais' }),
            'image'     : FileInput(attrs={'placeholder': 'image', }),
        }