from rest_framework.viewsets import ModelViewSet

from fabricahub.models import PerformanceLog
from fabricahub.serializers import PerformanceLogSerializer


class PerformanceLogViewSet(ModelViewSet):
    queryset = PerformanceLog.objects.select_related(
        "membro__usuario",
        "projeto",
    ).all()
    serializer_class = PerformanceLogSerializer