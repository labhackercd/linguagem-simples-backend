from django.utils.translation import ugettext_lazy as _
from django.urls import path, re_path
from rest_framework_simplejwt import views as jwt_views
from .views import ObtainTokenPairWithUsernameView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Linguagem Simples API",
        default_version='v1',
        description="Este projeto tem como finalidade um painel interativo \
                    para criação, edição e gestão de publicações do ACOMPANHE, \
                    com acesso rápido a informações e conteúdos produzidos \
                    pela casa e por canais de interesse.",
        contact=openapi.Contact(email="labhacker@camara.leg.br"),
        license=openapi.License(name="GNU General Public License v3.0"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
    path('token/obtain/', ObtainTokenPairWithUsernameView.as_view(),
         name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('token/verify/', jwt_views.TokenVerifyView.as_view(),
         name='token_verify'),
]