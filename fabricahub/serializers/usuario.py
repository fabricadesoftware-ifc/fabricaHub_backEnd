# Template para os serializers 
from rest_framework.serializers import ModelSerializer
from fabricahub.models import Usuario


class UsuarioSerializer(ModelSerializer):
    class Meta:
            model = Usuario
            # Liste os campos que você quer receber do frontend
            fields = ['id', 'username', 'email', 'password', 'tipo_usuario', 'first_name']
            
            # IMPORTANTE: Isso garante que a senha só pode ser escrita (POST), 
            # mas nunca vai aparecer na resposta (GET), por segurança!
            extra_kwargs = {
                'password': {'write_only': True}
            }

    def create(self, validated_data):
        # 1. Tiramos a senha de dentro do dicionário de dados validados
        password = validated_data.pop('password', None)
        
        # 2. Criamos o usuário normalmente com os dados restantes (username, tipo, etc)
        # O super().create() faz a criação padrão do ModelSerializer
        usuario = super().create(validated_data)
        
        # 3. Aplicamos a criptografia se a senha foi enviada
        if password:
            usuario.set_password(password)
            usuario.save() # Salvamos novamente no banco com o hash
            
        return usuario