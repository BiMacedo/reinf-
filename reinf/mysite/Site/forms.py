from django import forms
from .models import usuarios as Mod_usuarios

class login(forms.ModelForm):
    senha = forms.CharField(label='senha', widget=forms.PasswordInput)

    class Meta: 
        model = Mod_usuarios
        fields = '__all__'