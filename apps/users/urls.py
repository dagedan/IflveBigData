from django.urls import path, include, re_path
from . import views
app_name = 'users'

urlpatterns = [
    # 用户注册 reverse(users:register)
    path('signup', views.RegisterView.as_view(), name="register"),
    path('login', views.LoginView.as_view(), name="login"),
    path('logout', views.LogoutView.as_view(), name="logout"),
    path('user/<username>/count', views.UsernameCountView.as_view()),
]