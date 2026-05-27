from rest_framework.viewsets import ModelViewSet

from fabricahub.models import ProjetoMembro
from fabricahub.serializers import ProjetoMembroSerializer

class ProjetoMembroViewSet(ModelViewSet):
    queryset = ProjetoMembro.objects.all()
    serializer_class = ProjetoMembroSerializer