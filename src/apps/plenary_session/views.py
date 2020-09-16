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
            'date': DATE_FILTERS,
            'created': DATE_FILTERS,
            'modified': DATE_FILTERS,
            'id': ['exact'],
            'location': ['exact'],
            'type_session': ['exact'],
            'situation_session': ['exact'],
            'enable': ['exact'],
            'id_session_dados_abertos': ['exact']}


class PlenarySessionViewSet(ModelViewSet):
    queryset = PlenarySession.objects.all()
    serializer_class = PlenarySessionSerializer
    filter_backends = [rest_framework.DjangoFilterBackend,
                       filters.OrderingFilter,
                       filters.SearchFilter]
    filterset_class = PlenarySessionFilter
    ordering_fields = '__all__'
    search_fields = ['resume']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PublicationFilter(FilterSet):
    class Meta:
        model = Publication
        fields = {
            'created': DATE_FILTERS,
            'modified': DATE_FILTERS,
            'id': ['exact'],
            'session__id': ['exact'],
            'author__id': ['exact'],
            'state': ['exact']}


class PublicationViewSet(ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    filter_backends = [rest_framework.DjangoFilterBackend,
                       filters.OrderingFilter,
                       filters.SearchFilter]
    filterset_class = PublicationFilter
    ordering_fields = '__all__'
    search_fields = ['content', 'tweet_id', 'image', 'title']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class SavedContentFilter(FilterSet):
    class Meta:
        model = SavedContent
        fields = {
            'created': DATE_FILTERS,
            'id': ['exact'],
            'session__id': ['exact'],
            'content_type': ['exact']}


class SavedContentViewSet(ModelViewSet):
    queryset = SavedContent.objects.all()
    serializer_class = SavedContentSerializer
    filter_backends = [rest_framework.DjangoFilterBackend,
                       filters.OrderingFilter,
                       filters.SearchFilter]
    filterset_class = SavedContentFilter
    ordering_fields = '__all__'
    search_fields = ['title', 'url', 'id_saved_content']
