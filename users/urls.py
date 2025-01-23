from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    # для получения access токена
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # для обновления refresh токена
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]