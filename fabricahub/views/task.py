from rest_framework.viewsets import ModelViewSet
from fabricahub.models import Task
from fabricahub.serializers import TaskSerializer, TaskReadSerializer

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    def get_serializer_class(self):
        # Se a requisição for de leitura (GET), usa o serializer com depth=1
        if self.action in ['list', 'retrieve']:
            return TaskReadSerializer
        return TaskSerializer