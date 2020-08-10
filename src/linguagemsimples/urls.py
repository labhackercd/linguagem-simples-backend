from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.generic import TemplateView

schema_view = get_schema_view(
    openapi.Info(
        title="Linguagem Simples API",
        default_version='v1',
        description="Este projeto tem como finalidade um painel interativo \
                    para criação, edição e gestão de publicações do \
                    ACOMPANHE, com acesso rápido a informações e conteúdos \
                    produzidos pela casa e por canais de interesse.",
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
    path('admin/', admin.site.urls),
    path('api/', include('apps.authentication.urls')),
    path('api/', include('apps.plenary_session.urls')),
    path('api/', include('apps.api_ditec.urls')),
    path('teste/', TemplateView.as_view(template_name="components/base.html")),
    path('', include('django.contrib.auth.urls')),
]
