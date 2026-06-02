from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.utils import timezone
from django.shortcuts import get_object_or_404

from fabricahub.models import Membro, Projeto, Task
from fabricahub.serializers import MembroSerializer


class MembroViewSet(ModelViewSet):
    queryset = Membro.objects.select_related("usuario").all()
    serializer_class = MembroSerializer

    @action(
        detail=False,
        methods=["get"],
        permission_classes=[IsAuthenticated],
        url_path="me"
    )
    def me(self, request):
        """
        Retorna os dados do membro autenticado.
        Rota: GET /api/membros/me/
        """

        membro = get_object_or_404(
            Membro.objects.select_related("usuario"),
            usuario=request.user
        )

        serializer = self.get_serializer(membro)

        return Response(serializer.data)

    @action(detail=False, methods=["get"], url_path="dashboard-metricas")
    def dashboard_metricas(self, request):
        """
        Retorna as métricas agregadas para a Dashboard do membro logado.
        Rota: GET /api/membros/dashboard-metricas/
        """

        user = request.user
        hoje = timezone.now()

        # 1. Projetos em Andamento do Usuário
        projetos_andamento = Projeto.objects.filter(
            projeto_membros__membro__usuario=user,
            status="em_andamento"
        ).distinct().count()

        # 2. Tarefas Concluídas no Mês Atual
        tarefas_concluidas = Task.objects.filter(
            projeto__projeto_membros__membro__usuario=user,
            status="CONCLUIDA",
            prazo__month=hoje.month,
            prazo__year=hoje.year
        ).distinct().count()

        # 3. Tarefas Pendentes Gerais
        tarefas_pendentes = Task.objects.filter(
            projeto__projeto_membros__membro__usuario=user,
            status="PENDENTE"
        ).distinct().count()

        payload = {
            "projetos_ativos": projetos_andamento,
            "tarefas_concluidas_mes": tarefas_concluidas,
            "tarefas_pendentes": tarefas_pendentes
        }

        return Response(payload)