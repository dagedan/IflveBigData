from django.urls import path, include
from . import views
app_name = 'index'

urlpatterns = [
    # 用户注册 reverse(users:register)
    path('', views.IndexView.as_view(), name="index"),
]