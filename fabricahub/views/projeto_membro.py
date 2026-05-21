from rest_framework.viewsets import ModelViewSet

from fabricahub.models import ProjetoMembro
from fabricahub.serializers import Projeto

class ProjetoViewSet(ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer