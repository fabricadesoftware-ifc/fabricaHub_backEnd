# Template para os serializers 
from rest_framework.serializers import ModelSerializer
from fabricahub.models import Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
    def get_serializer_class(self):
        return super().get_serializer_class()
    
class TaskReadSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        depth = 1 # Traz os detalhes do Projeto e do Responsável (Membro) mastigados no GET 