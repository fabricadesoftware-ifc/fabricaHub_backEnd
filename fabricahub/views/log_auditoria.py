from rest_framework.viewsets import ModelViewSet
from fabricahub.models import LogAuditoria
from fabricahub.serializers import LogAuditoriaSerializer

class LogAuditoriaViewSet(ModelViewSet):
    queryset = LogAuditoria.objects.select_related(
        "operador__usuario",
    ).all()
    
    serializer_class = LogAuditoriaSerializer