from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from users.views import AccoutView

urlpatterns = [
    path('login/', obtain_auth_token, name='token'),
    path('account/', AccoutView.as_view(), name='account')
]