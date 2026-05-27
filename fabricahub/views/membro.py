from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from django.utils import timezone
from django.db.models import Count, Q

from fabricahub.models import Membro, Projeto
from fabricahub.serializers import MembroSerializer


class MembroViewSet(ModelViewSet):
    queryset = Membro.objects.select_related("usuario").all()
    serializer_class = MembroSerializer
    
    @action(detail=False, methods=['get'])
    def dashboard_metrics(self, request):
        user = request.user
        mes_atual = timezone.now().month
        
        projetos_ativos = Projeto.objects,filter(
            membros__usuario=user,
            status='em_andamento'
        ).count()
        
        # tarefas_concluidas_mes = Tarefa.objects.filter(
        #     responsavel=user,
        #     status='concluida',
        #     data_fim__month=mes_atual
        # ).count()
        
        return Response({
            "projetos_ativos": projetos_ativos,
            # "tarefas_concluidas_mes": tarefas_concluidas_mes,
        })
