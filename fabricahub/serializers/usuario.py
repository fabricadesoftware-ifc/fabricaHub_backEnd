# Template para os serializers 
from rest_framework.serializers import ModelSerializer
from fabricahub.models import Usuario


class UsuarioSerializer(ModelSerializer):
    class Meta:
            model = Usuario
            fields = ['id', 'username', 'email', 'password', 'tipo_usuario', 'first_name']
            
            extra_kwargs = {
                'password': {'write_only': True}
            }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        
        usuario = super().create(validated_data)
        
        if password:
            usuario.set_password(password)
            usuario.save() 
            
        return usuario