from django.urls import path, include

from . import views

urlpatterns = [
    # 用户注册 reverse(users:register)
    path('register', views.RegisterView.as_view(), name="register")
]