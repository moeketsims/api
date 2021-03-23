from django.urls import path
from .views import UploadView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', UploadView, basename='upload')
urlpatterns = router.urls
