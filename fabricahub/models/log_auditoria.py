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
    entidade_id = models.UUIDField(null=True, blank=True)
    detalhes = models.TextField(blank=True)

    class Meta:
        verbose_name = "Log de Auditoria"
        verbose_name_plural = "Logs de Auditoria"
        ordering = ["-created_at"]

    def __str__(self):
        # Evita quebrar se o log acabou de ser instanciado e não foi salvo no banco ainda
        data_formatada = self.created_at.strftime('%d/%m/%Y %H:%M') if self.created_at else "Agora"
        operador_nome = self.operador if self.operador else "Sistema/Anônimo"
        
        return f"({data_formatada}) - {operador_nome} - {self.acao} - {self.entidade_afetada}({self.entidade_id})"