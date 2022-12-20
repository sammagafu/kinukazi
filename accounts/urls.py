from django.urls import path
from .views import MyObtainTokenPairView
from rest_framework_simplejwt.views import TokenRefreshView
from . import views


urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('users/', views.Users.as_view(), name='user_list'),
    path('users/me/', views.UserProfile.as_view(), name='user_profile'),
    path('users/me/update-avatar/', views.UpdateUserProfilePicture.as_view(), name='update'),
    path('users/<str:memberId>/', views.UsersDetail.as_view(), name='user'),

]