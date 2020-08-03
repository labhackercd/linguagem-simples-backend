from django.urls import path
from .views import ListNews

urlpatterns = [
    path('news/', ListNews.as_view(),
         name='news-list'),
]
