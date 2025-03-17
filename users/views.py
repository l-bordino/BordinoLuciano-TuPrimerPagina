from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login as django_login
from django.urls import reverse_lazy
from users.forms import MoviePasswordChangeForm, MovieUserCreationForm, MovieUserChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User

from users.models import AdditionalInfo

def login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            user_logged = formulario.get_user()
            
            django_login(request,user_logged)
            
            AdditionalInfo.objects.get_or_create(user=user_logged)
            
            return redirect('inicio')
    else:
        formulario = AuthenticationForm()
    return render(request, 'users/login.html', {'formulario': formulario} )

def register(request):
    
    if request.method == 'POST':
        
        formulario = MovieUserCreationForm(request.POST)
        
        if formulario.is_valid():
            user = formulario.save()
            favorite_genre = formulario.cleaned_data.get('favorite_genre')
            AdditionalInfo.objects.create(user=user, favorite_genre=favorite_genre)
            return redirect('login')
    else:
        formulario = MovieUserCreationForm()
        
    return render(request, 'users/register.html', {'formulario': formulario} )

def edit_user(request):
    
    add_info = request.user.additionalinfo
    
    if request.method == 'POST':
        
        formulario = MovieUserChangeForm(request.POST, request.FILES, instance=request.user)
        
        if formulario.is_valid():
            
            if formulario.cleaned_data.get('avatar'):
                add_info.avatar =  formulario.cleaned_data.get('avatar')
            
            add_info.favorite_genre = formulario.cleaned_data.get('favorite_genre')
            add_info.save()
            formulario.save()
            
            return redirect('inicio')
    else:
        formulario = MovieUserChangeForm(instance=request.user, initial={'avatar': add_info.avatar, 'favorite_genre': add_info.favorite_genre})
        
    return render(request, 'users/edit_user.html', {'formulario': formulario} )

class MoviePasswordChangeView(PasswordChangeView):
    form_class = MoviePasswordChangeForm
    template_name = 'users/change_pw.html'
    success_url = reverse_lazy('login')
    
class UserInfoView(DetailView):
    model = User
    template_name = 'users/user_info.html'
    context_object_name = 'usuario'

    def get_object(self):
        return self.request.user
