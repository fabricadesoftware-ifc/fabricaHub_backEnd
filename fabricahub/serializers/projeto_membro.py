# Template para os serializers 
from rest_framework.serializers import ModelSerializer
from fabricahub.models import ProjetoMembro


class ProjetoMembroSerializer(ModelSerializer):
    class Meta:
        model = ProjetoMembro
        fields = '__all__'