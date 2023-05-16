from django.urls import path
from .views import UpdateUser, CreateUser
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('update/', UpdateUser.as_view(), name='update_user'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', CreateUser.as_view(), name='register')
]
