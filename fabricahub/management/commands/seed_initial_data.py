from datetime import date

from django.core.management.base import BaseCommand

from fabricahub.models import Membro, PerformanceLog, Projeto, Usuario


class Command(BaseCommand):
    help = "Cria dados iniciais para desenvolvimento"

    def handle(self, *args, **kwargs):
        usuario, created = Usuario.objects.get_or_create(
            username="arthur",
            defaults={
                "first_name": "Arthur",
                "last_name": "Lanz",
                "email": "arthur@example.com",
                "tipo_usuario": Usuario.TipoUsuario.MEMBRO,
            },
        )

        if created:
            usuario.set_password("123456")
            usuario.save()

        membro, _ = Membro.objects.get_or_create(
            usuario=usuario,
            defaults={
                "curso": "Sistemas de Informação",
                "semestre": 2,
                "squad": Membro.Squad.BACKEND,
            },
        )

        projeto, _ = Projeto.objects.get_or_create(
            nome="FabricaHub",
            defaults={
                "descricao_tecnica": "API REST com Django e DRF",
                "status": Projeto.Status.EM_ANDAMENTO,
                "data_inicio": date(2026, 5, 15),
                "prazo_entrega": date(2026, 12, 1),
            },
        )

        projeto.membros.add(membro)

        PerformanceLog.objects.get_or_create(
            membro=membro,
            projeto=projeto,
            contexto_entrega="Entrega inicial da API business",
            defaults={
                "metrica_entrega": 9.50,
                "observacao": "Seed inicial para desenvolvimento",
            },
        )

        self.stdout.write(self.style.SUCCESS("Seed inicial carregada com sucesso."))