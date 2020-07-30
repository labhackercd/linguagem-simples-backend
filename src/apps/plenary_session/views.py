from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import PlenarySession, Publication
from .serializers import PlenarySessionSerializer, PublicationSerializer


class PlenarySessionViewSet(viewsets.ModelViewSet):
    queryset = PlenarySession.objects.all()
    serializer_class = PlenarySessionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
