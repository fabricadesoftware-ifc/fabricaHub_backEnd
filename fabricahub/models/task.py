from django.db import models
from fabricahub.models import BaseModel, Projeto, Membro
class Task(BaseModel):
    class Status(models.TextChoices):
        PENDENTE = 'PENDENTE', 'Pendente'
        EM_ANDAMENTO = 'EM_ANDAMENTO', 'Em Andamento'
        CONCLUIDA = 'CONCLUIDA', 'Concluída'
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDENTE)
    prazo = models.DateField(null=True, blank=True)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    responsavel = models.ForeignKey(Membro, on_delete=models.SET_NULL, null=True, blank=True)
    class Meta:
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"
        ordering = ["prazo", "projeto", "status"]
    def __str__(self):
        return f"{self.titulo} - {self.get_status_display()}"