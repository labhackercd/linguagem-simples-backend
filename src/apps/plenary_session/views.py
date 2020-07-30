from rest_framework import viewsets
from .models import PlenarySession, Publication
from .serializers import PlenarySessionSerializer, PublicationSerializer


class PlenarySessionViewSet(viewsets.ModelViewSet):
    queryset = PlenarySession.objects.all()
    serializer_class = PlenarySessionSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
