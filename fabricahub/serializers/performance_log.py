from rest_framework import serializers

from fabricahub.models import PerformanceLog


class PerformanceLogSerializer(serializers.ModelSerializer):
    membro_nome = serializers.CharField(source="membro.usuario.username", read_only=True)
    projeto_nome = serializers.CharField(source="projeto.nome", read_only=True)

    class Meta:
        model = PerformanceLog
        fields = [
            "id",
            "membro",
            "membro_nome",
            "projeto",
            "projeto_nome",
            "contexto_entrega",
            "metrica_entrega",
            "observacao",
            "created_at",
            "updated_at",
        ]