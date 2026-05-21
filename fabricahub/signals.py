from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from fabricahub.models import Task, LogAuditoria, Projeto, ProjetoMembro

@receiver(post_save, sender=Task)
def auditar_task(sender, instance, created, **kwargs):
    """
    Sempre que uma Task for criada ou atualizada. 
    """
    acao = "Tarefa Criada" if created else "Tarefa Atualizada"

    LogAuditoria.objects.create(
        operador=instance.responsavel,
        acao=acao,
        entidade_afetada="Task",
        entidade_id=instance.id,
        detalhes=f"A Tarefa '{instance.titulo}' vinculada ao projeto '{instance.projeto}' com o status '{instance.get_status_display()}'."
    )

@receiver(post_save, sender=Projeto)
def encerrar_projeto_finalizado(sender, instance, created, **kwargs):
    """
    Caso o projeto mude de status para 'Finalizado', 
    atualiza a data_fim de todos os vínculos na tabela intermediária.
    """
    if instance.status == Projeto.Status.FINALIZADO:
        ProjetoMembro.objects.filter(
            projeto=instance.id,
            data_fim__isnull=True
        ).update(data_fim=timezone.now().date())