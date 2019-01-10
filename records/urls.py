from rest_framework.routers import SimpleRouter

from records.views import RecordViewSet

router = SimpleRouter()

router.register('records', RecordViewSet, 'records')

urlpatterns = []

urlpatterns += router.urls