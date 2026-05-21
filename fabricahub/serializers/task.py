# Template para os serializers 
from rest_framework.serializers import ModelSerializer
from fabricahub.models import Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'