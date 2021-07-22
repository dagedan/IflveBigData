from django.urls import path, include, re_path
from . import views
app_name = 'verifications'

urlpatterns = [
    path('verifications/<uuid>', views.ImgVerificationsView.as_view(), name="code"),
]