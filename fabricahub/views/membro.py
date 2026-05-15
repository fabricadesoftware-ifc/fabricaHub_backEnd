from rest_framework.viewsets import ModelViewSet

from fabricahub.models import Membro
from fabricahub.serializers import MembroSerializer


class MembroViewSet(ModelViewSet):
    queryset = Membro.objects.select_related("usuario").all()
    serializer_class = MembroSerializer