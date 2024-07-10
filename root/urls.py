from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf.urls.static import static
from django.conf import settings

# from app.views.translation_conf import set_language
from app.trasnlation_01 import set_language

schema_view = get_schema_view(
    openapi.Info(
        title="Drf-E_commerce Snippets API",
        default_version='v1',
        description="Template for DRF",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
                  path('abduvali/', admin.site.urls),
                  path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  path('', include("app.urls")),
                  path('api-auth/', include('rest_framework.urls')),
                  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),

    path("set_language/<str:language>", set_language, name="set-language"),

]
