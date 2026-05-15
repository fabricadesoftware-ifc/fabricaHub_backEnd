from django.db import models

from fabricahub.models.base import BaseModel
from fabricahub.models.membro import Membro
from fabricahub.models.projeto import Projeto


class PerformanceLog(BaseModel):
    membro = models.ForeignKey(
        Membro,
        on_delete=models.CASCADE,
        related_name="performance_logs",
    )
    projeto = models.ForeignKey(
        Projeto,
        on_delete=models.CASCADE,
        related_name="performance_logs",
    )
    contexto_entrega = models.TextField()
    metrica_entrega = models.DecimalField(max_digits=5, decimal_places=2)
    observacao = models.TextField(blank=True)

    class Meta:
        verbose_name = "Registro de Performance"
        verbose_name_plural = "Registros de Performance"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.membro} - {self.projeto}"