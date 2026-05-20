from django.db import models

from fabricahub.models.base import BaseModel
from fabricahub.models.usuario import Usuario


class Membro(BaseModel):
    class Squad(models.TextChoices):
        BACKEND = "backend", "Backend"
        FRONTEND = "frontend", "Frontend"
        DESIGN = "design", "Design"
        DEVOPS = "devops", "DevOps"

    usuario = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        related_name="membro",
    )
    curso = models.CharField(max_length=120)
    semestre = models.PositiveIntegerField()
    squad = models.CharField(max_length=30, choices=Squad.choices)

    class Meta:
        verbose_name = "Membro"
        verbose_name_plural = "Membros"
        ordering = ["usuario__first_name", "usuario__username"]

    def __str__(self):
        return self.usuario.get_full_name() or self.usuario.username