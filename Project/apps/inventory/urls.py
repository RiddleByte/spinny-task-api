from rest_framework import routers

from .views import BoxViewSet

router = routers.SimpleRouter()
router.register(r"boxes", BoxViewSet, basename="box")
urlpatterns = router.urls
