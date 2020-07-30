from rest_framework import routers
from .views import PlenarySessionViewSet, PublicationViewSet


router = routers.SimpleRouter()
router.register(r'sessions', PlenarySessionViewSet, basename='sessions')
router.register(r'publications', PublicationViewSet, basename='publications')

urlpatterns = router.urls
