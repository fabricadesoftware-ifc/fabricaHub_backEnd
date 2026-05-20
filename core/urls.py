from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from fabricahub.views import (
    MembroViewSet,
    PerformanceLogViewSet,
    ProjetoViewSet,
    UsuarioViewSet,
)

router = DefaultRouter()
router.register(r"usuarios", UsuarioViewSet, basename="usuario")
router.register(r"membros", MembroViewSet, basename="membro")
router.register(r"projetos", ProjetoViewSet, basename="projeto")
router.register(r"performance-logs", PerformanceLogViewSet, basename="performance-log")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]