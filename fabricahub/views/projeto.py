from django.db.models import Prefetch
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from fabricahub.permissions import IsProjectMember
from fabricahub.models import Membro, Projeto
from fabricahub.serializers import ProjetoSerializer


class ProjetoViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsProjectMember]
    serializer_class = ProjetoSerializer
    def get_queryset(self):
        user= self.request.user
        
        base_queryset = Projeto.objects.prefetch_related(
            Prefetch(
            "membros",
            queryset=Membro.objects.select_related("usuario"),
            )
        )
        
        if user.is_superuser:
            return base_queryset.all()
        
        return base_queryset.filter(membros__usuario=user).distinct()
    
    
