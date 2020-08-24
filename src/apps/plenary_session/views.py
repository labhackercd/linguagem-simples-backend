from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from .models import PlenarySession, Publication, SavedContent
from .serializers import (PlenarySessionSerializer, PublicationSerializer,
                          SavedContentSerializer)
from django_filters import rest_framework, FilterSet


DATE_FILTERS = ['exact', 'lt', 'gt', 'lte',
                'gte', 'year__exact', 'month__exact']


class PlenarySessionFilter(FilterSet):
    class Meta:
        model = PlenarySession
        fields = {
            'date': DATE_FILTERS}


class PlenarySessionViewSet(ModelViewSet):
    queryset = PlenarySession.objects.all()
    serializer_class = PlenarySessionSerializer
    filter_backends = [rest_framework.DjangoFilterBackend,
                       filters.OrderingFilter]
    filterset_class = PlenarySessionFilter
    ordering_fields = ['date']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PublicationFilter(FilterSet):
    class Meta:
        model = Publication
        fields = {
            'created': DATE_FILTERS,
            'state': ['exact']}


class PublicationViewSet(ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    filter_backends = [rest_framework.DjangoFilterBackend,
                       filters.OrderingFilter,
                       filters.SearchFilter]
    filterset_class = PublicationFilter
    ordering_fields = ['created']
    search_fields = ['content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class SavedContentFilter(FilterSet):
    class Meta:
        model = SavedContent
        fields = {
            'created': DATE_FILTERS,
            'content_type': ['exact']}


class SavedContentViewSet(ModelViewSet):
    queryset = SavedContent.objects.all()
    serializer_class = SavedContentSerializer
    filter_backends = [rest_framework.DjangoFilterBackend,
                       filters.OrderingFilter,
                       filters.SearchFilter]
    filterset_class = SavedContentFilter
    ordering_fields = ['created']
    search_fields = ['title']
