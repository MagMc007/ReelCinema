from django.urls import path
from rest_framework import routers
from .views import ReviewView

router = routers.DefaultRouter()
router.register(r"rev", ReviewView, basename="review")
urlpatterns = router.urls