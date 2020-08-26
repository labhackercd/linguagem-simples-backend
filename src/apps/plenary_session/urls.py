from rest_framework import routers
from .views import (PlenarySessionViewSet, PublicationViewSet,
                    SavedContentViewSet)


router = routers.SimpleRouter()
router.register(r'sessions', PlenarySessionViewSet, basename='sessions')
router.register(r'publications', PublicationViewSet, basename='publications')
router.register(r'saved-contents', SavedContentViewSet,
                basename='saved-contents')

urlpatterns = router.urls
