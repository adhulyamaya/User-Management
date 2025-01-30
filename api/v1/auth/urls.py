from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

app_name = 'user_api'

urlpatterns = [
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/', views.UserTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # path('login/', views.login_view, name='login'),
    # path('mislogin/', views.mis_login, name='mislogin'),
]
