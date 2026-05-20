from datetime import date

from django.core.management.base import BaseCommand

from fabricahub.models import Membro, LogAuditoria, Projeto, Usuario, ProjetoMembro


class Command(BaseCommand):
    help = "Cria dados iniciais para desenvolvimento"

    def handle(self, *args, **kwargs):
        usuario, created = Usuario.objects.get_or_create(
            username="fabrica",
            defaults={
                "first_name": "Fabrica",
                "last_name": "de Software",
                "email": "fabricadesoftware@ifc.edu.br",
                "tipo_usuario": Usuario.TipoUsuario.TECHLEAD,
            },
        )

        if created:
            usuario.set_password("fabrica")
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
 
        ProjetoMembro.objects.get_or_create(
            projeto=projeto,
            membro=membro,
            defaults={
                "papel_no_projeto": "Desenvolvedor Backend",
                "data_entrada": date(2026, 5, 15),
            }
        )

        LogAuditoria.objects.get_or_create(
            operador=membro,
            acao="Criação Inicial de Projeto",
            entidade_afetada="Projeto",
            entidade_id=projeto.id,  # Salvamos apenas o ID do projeto de forma genérica
            defaults={
                "detalhes": f"Entrega inicial da API business para o projeto {projeto.nome}. Métrica antiga: 9.50. Observação: Seed inicial para desenvolvimento",
            },
        )

        self.stdout.write(self.style.SUCCESS("Seed inicial carregada com sucesso."))