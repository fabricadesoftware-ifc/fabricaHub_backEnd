from django.db.models import Prefetch
from rest_framework.viewsets import ModelViewSet

from fabricahub.models import Membro, Projeto
from fabricahub.serializers import ProjetoSerializer


class ProjetoViewSet(ModelViewSet):
    queryset = Projeto.objects.prefetch_related(
        Prefetch(
            "membros",
            queryset=Membro.objects.select_related("usuario"),
        )
    ).all()
    serializer_class = ProjetoSerializer