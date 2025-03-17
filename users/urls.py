from django.urls import path
from users.views import MoviePasswordChangeView, UserInfoView, login, register, edit_user
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('edit-user/', edit_user, name='edit_user'),
    path('edit-user/change-pw', MoviePasswordChangeView.as_view(), name='change_pw'),
    path('user-info/', UserInfoView.as_view(), name='user_info'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
