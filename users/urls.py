from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import SimpleRouter

from users.views import UserViewSet

router = SimpleRouter()

router.register(r'users', UserViewSet)

urlpatterns = [
    path('login/', obtain_auth_token, name='token')
]

urlpatterns += router.urls