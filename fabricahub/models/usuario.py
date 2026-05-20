# Template para os models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _  # <--- Add this import
class Usuario(AbstractUser):
    class TipoUsuario(models.IntegerChoices):
        MEMBRO = 1, "Membro"
        PROFESSOR = 2, "Professor"
        TECHLEAD = 3, "Techlead"
    tipo_usuario = models.IntegerField(choices=TipoUsuario.choices, default=TipoUsuario.MEMBRO, verbose_name=_("Tipo de Usuário"))
    def __str__(self):
        return self.first_name