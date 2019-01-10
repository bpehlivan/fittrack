from django.urls import path, include

urlpatterns = [
    path('auth/', include(('users.urls', 'users'), namespace='auth')),
    path('app/', include(('records.urls', 'records'), namespace='app'))
]
