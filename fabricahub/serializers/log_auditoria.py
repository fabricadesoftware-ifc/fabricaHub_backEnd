from rest_framework import serializers
from fabricahub.models import LogAuditoria


class LogAuditoriaSerializer(serializers.ModelSerializer):
    operador_username = serializers.CharField(
        source="operador.usuario.username", 
        read_only=True, 
        default="Sistema"
    )
    operador_nome = serializers.CharField(
        source="operador.usuario.get_full_name", 
        read_only=True, 
        default="Sistema"
    )
    class Meta:
        model = LogAuditoria
        fields = [
            "id",
            "operador",
            "operador_username",
            "operador_nome",
            "acao",
            "entidade_afetada",
            "entidade_id",
            "detalhes",
            "created_at",
            "updated_at",
        ]
        depth = 1