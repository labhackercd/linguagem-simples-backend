from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import PlenarySession
from .serializers import PlenarySessionSerializer


class PlenarySessionViewSet(viewsets.ModelViewSet):
    queryset = PlenarySession.objects.all()
    serializer_class = PlenarySessionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
