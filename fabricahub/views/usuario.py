from rest_framework.viewsets import ModelViewSet
from fabricahub.models import Usuario
from fabricahub.serializers.usuario import UsuarioSerializer

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer