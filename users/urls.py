from django.urls import path
from users import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('signup/', views.UserView.as_view(), name="user_view"),
    path('info/', views.InfoView.as_view(), name="info_view"),
    path('mock/', views.mockView.as_view(), name="mock_view"),
    path('api/token/', views.CustomTokenObtainPairView.as_view(),
         name="token_obtain_pair"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
]
