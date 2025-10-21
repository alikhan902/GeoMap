from rest_framework.routers import DefaultRouter
from .views import PlaceDetailAPIView

router = DefaultRouter()
router.register(r'places', PlaceDetailAPIView, basename='places')

urlpatterns = router.urls