from django.db import models

from fabricahub.models.base import BaseModel
from fabricahub.models.membro import Membro


class Projeto(BaseModel):
    class Status(models.TextChoices):
        PLANEJAMENTO = "planejamento", "Planejamento"
        EM_ANDAMENTO = "em_andamento", "Em andamento"
        FINALIZADO = "finalizado", "Finalizado"
        CANCELADO = "cancelado", "Cancelado"

    nome = models.CharField(max_length=150)
    descricao_tecnica = models.TextField()
    status = models.CharField(
        max_length=30,
        choices=Status.choices,
        default=Status.PLANEJAMENTO,
    )
    data_inicio = models.DateField()
    prazo_entrega = models.DateField()
    # membros = models.ManyToManyField(
    #     Membro,
    #     related_name="projetos",
    #     blank=True,
    # )

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"
        ordering = ["prazo_entrega", "nome"]

    def __str__(self):
        return self.nome