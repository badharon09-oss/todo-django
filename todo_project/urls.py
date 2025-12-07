from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),            # tasks endpoints
    path('api/auth/', include('rest_framework.urls')),  # browsable API login
    # if using simplejwt, add token endpoints:
    # path('api/auth/', include('users.urls')),    # if you create custom auth endpoints
]

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns += [
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
