from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

from inicio.models import Movie

class MovieUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    favorite_genre = forms.ChoiceField(choices=[("", "---")] + Movie.GENRE_CHOICES, required=False)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {field:'' for field in fields}
        
class MovieUserChangeForm(UserChangeForm):
    password = None
    email = forms.EmailField()
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    favorite_genre = forms.ChoiceField(choices=[("", "---")] + Movie.GENRE_CHOICES, required=False, label="Género favorito")
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'avatar']   
        
class MoviePasswordChangeForm(PasswordChangeForm):
    
    old_password = forms.CharField(label='Contraseña vieja', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='Ingrese su nueva contraseña', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Ingresela de nuevo', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        help_texts = {field:'' for field in fields}