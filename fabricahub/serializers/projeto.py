from rest_framework import serializers

from fabricahub.models import Projeto


class ProjetoSerializer(serializers.ModelSerializer):
    membros_detalhes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Projeto
        fields = [
            "id",
            "nome",
            "descricao_tecnica",
            "status",
            "data_inicio",
            "prazo_entrega",
            "membros",
            "membros_detalhes",
            "created_at",
            "updated_at",
        ]

    def get_membros_detalhes(self, obj):
        return [
            {
                "id": membro.id,
                "nome": membro.usuario.get_full_name() or membro.usuario.username,
                "username": membro.usuario.username,
                "squad": membro.squad,
            }
            for membro in obj.membros.all()
        ]