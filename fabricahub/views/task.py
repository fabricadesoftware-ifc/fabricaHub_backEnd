from rest_framework.viewsets import ModelViewSet

from fabricahub.models import Task
from fabricahub.serializers import TaskSerializer

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer