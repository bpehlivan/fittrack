from django.urls import path
from rest_framework.routers import SimpleRouter

from users.views import UserRegisterViewSet, PasswordResetViewSet, Activation

router = SimpleRouter()

router.register(r'register', UserRegisterViewSet)
router.register(r'reset', PasswordResetViewSet)

urlpatterns = [
    path('activation', Activation.as_view(), name='activation')
]

urlpatterns += router.urls
