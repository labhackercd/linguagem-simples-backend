from django.urls import path, include
from rest_framework import routers
from .views import PlenarySessionViewSet


router = routers.SimpleRouter()
router.register(r'sessoes', PlenarySessionViewSet, basename='sessoes')

urlpatterns = router.urls
