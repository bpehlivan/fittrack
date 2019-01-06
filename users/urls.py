from django.urls import path
from rest_framework.routers import SimpleRouter

from users.views import UserViewSet

router = SimpleRouter()

router.register(r'register', UserViewSet)

urlpatterns = [
]

urlpatterns += router.urls
