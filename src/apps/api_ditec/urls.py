from django.urls import path
from .views import ListNews, SearchNews, ListRadioagency, SearchRadioagency

urlpatterns = [
    path('news/', ListNews.as_view(), name='news'),
    path('news-search/', SearchNews.as_view(), name='news-search'),
    path('radioagency/', ListRadioagency.as_view(), name='radioagency'),
    path('radioagency-search/', SearchRadioagency.as_view(),
         name='radioagency-search'),
]
