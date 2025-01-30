from django.urls import path
from . import views

app_name = 'user_api'

urlpatterns = [
    path('main-admin/login/', views.main_admin_login, name='main_admin_login'),
]
