from django.urls import path
from .views import (ListNews, SearchNews, ListRadioagency, SearchRadioagency,
                    ListTvCamara, SearchTvCamara, ListRadioCamara,
                    SearchRadioCamara)

urlpatterns = [
    path('news/', ListNews.as_view(), name='news'),
    path('news-search/', SearchNews.as_view(), name='news-search'),
    path('radioagency/', ListRadioagency.as_view(), name='radioagency'),
    path('radioagency-search/', SearchRadioagency.as_view(),
         name='radioagency-search'),
    path('tvcamara/', ListTvCamara.as_view(), name='tvcamara'),
    path('tvcamara-search/', SearchTvCamara.as_view(),
         name='tvcamara-search'),
    path('radiocamara/', ListRadioCamara.as_view(), name='radiocamara'),
    path('radiocamara-search/', SearchRadioCamara.as_view(),
         name='radiocamara-search'),
]
