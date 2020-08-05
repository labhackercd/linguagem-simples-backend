from django.urls import path
from .views import ListNews, SearchNews

urlpatterns = [
    path('news/', ListNews.as_view(), name='news'),
    path('news-search/', SearchNews.as_view(), name='news-search'),
]
