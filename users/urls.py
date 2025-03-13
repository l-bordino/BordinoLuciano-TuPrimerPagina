from django.urls import path
from users.views import ChangePassword, login, register, edit_user
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('edit-user/', edit_user, name='edit_user'),
    path('edit-user/change-pw', ChangePassword.as_view(), name='change_pw'),
]
