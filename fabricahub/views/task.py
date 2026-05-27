from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from fabricahub.models import Task
from fabricahub.serializers import TaskSerializer, TaskReadSerializer
from fabricahub.filters import TaskFilter
from fabricahub.permissions import IsProjectMember

# class TaskViewSet(ModelViewSet):
#     queryset = Task.objects.all()
#     def get_serializer_class(self):
#         # Se a requisição for de leitura (GET), usa o serializer com depth=1
#         if self.action in ['list', 'retrieve']:
#             return TaskReadSerializer
#         return TaskSerializer

class TaskViewSet(ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter
    permission_classes = [IsProjectMember] 

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return TaskReadSerializer
        return TaskSerializer

    def get_queryset(self):
        user = self.request.user
        
        # Se for admin (super user), vê todas as tarefas de todos os projetos
        if user.is_superuser:
            return Task.objects.all()
            
        # O pulo do gato da filtragem: 
        # Busca tarefas onde o 'projeto' tem um vínculo em 'projeto_membros' 
        # que pertence ao 'membro' que está atrelado ao 'usuario' logado.
        return Task.objects.filter(
            projeto__projeto_membros__membro__usuario=user
        ).distinct()