from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include(('api.v1.auth.urls'),namespace='auth_api')),
    path('api/v1/customer/', include(('api.v1.customer_api.urls'),namespace='customer_api')),
    path('api/v1/financial/', include(('api.v1.financial_api.urls'),namespace='financial_api')),
    # path('api/v1/main_admin/', include(('api.v1.main_admin_api.urls'),namespace='main_admin_api')),
    path('api/v1/reports/', include(('api.v1.reports_api.urls'),namespace='reports_api')),
    path('api/v1/services/', include(('api.v1.services_api.urls'),namespace='services_api')),
    path('api/v1/users/', include(('api.v1.user_api.urls'),namespace='user_api'))  
]
