from django.db import models
from fabricahub.models import BaseModel

class LogAuditoria(BaseModel):
    operador = models.ForeignKey(
        'fabricahub.Membro',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="auditoria_logs"
    )
    acao = models.CharField(max_length=255)

    entidade_afetada = models.CharField(max_length=255)
    entidade_id = models.PositiveIntegerField(null=True, blank=True)

    detalhes = models.TextField(blank=True)

    class Meta:
        verbose_name = "Log de Auditoria"
        verbose_name_plural = "Logs de Auditoria"
        ordering = ["-created_at"]
    def __str__(self):
        return f"({self.created_at.strftime('%d/%m/%Y %H:%M')}) - {self.operador} - {self.acao} - {self.entidade_afetada}({self.entidade_id})"