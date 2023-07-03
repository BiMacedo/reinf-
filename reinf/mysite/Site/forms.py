from django import forms
from .models import usuario as Mod_usuario

class login(forms.ModelForm):
    senha = forms.CharField(label='senha', widget=forms.PasswordInput)

    class Meta: 
        model = Mod_usuario
        fields = '__all__'