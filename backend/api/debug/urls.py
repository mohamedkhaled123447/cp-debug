# Desc: URL patterns for the debug app
from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter
router=SimpleRouter()
router.register('profile',views.profileViewSet,basename='profile')
urlpatterns = router.urls