from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ItemsViewSet

router = DefaultRouter()
router.register(r'items', ItemsViewSet)

urlpatterns = router.urls
