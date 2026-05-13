# Template para os serializers 
from rest_framework.serializers import ModelSerializer
from fabricahub.models import Usuario


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'