from django.urls import path, include, re_path
from . import views
app_name = 'users'

urlpatterns = [
    # 用户注册 reverse(users:register)
    path('register', views.RegisterView.as_view(), name="register"),
    path('login', views.LoginView.as_view(), name="login"),
    re_path('/usernames/<username:username>/count', views.UsernameCountView())
]