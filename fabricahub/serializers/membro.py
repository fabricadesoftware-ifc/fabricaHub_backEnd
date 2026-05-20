from rest_framework import serializers

from fabricahub.models import Membro


class MembroSerializer(serializers.ModelSerializer):
    usuario_nome = serializers.CharField(source="usuario.get_full_name", read_only=True)
    usuario_username = serializers.CharField(source="usuario.username", read_only=True)

    class Meta:
        model = Membro
        fields = [
            "id",
            "usuario",
            "usuario_nome",
            "usuario_username",
            "curso",
            "semestre",
            "squad",
            "created_at",
            "updated_at",
        ]