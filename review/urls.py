from django.urls import path
from rest_framework import routers
from .views import ReviewView

router = routers.DefaultRouter()
router.register(r"review", ReviewView, basename="review")
urlpatterns = router.urls