from django.urls import path 
from rest_framework_simplejwt import views as jwt_views 
from users.views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
	path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'), 
	path('refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh')
] 
