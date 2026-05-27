from django.db import models
from fabricahub.models import BaseModel, Projeto, Membro

class ProjetoMembro(BaseModel):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name="projeto_membros")
    membro = models.ForeignKey(Membro, on_delete=models.CASCADE, related_name="membro_projetos")
    data_entrada = models.DateField()
    data_saida = models.DateField(null=True, blank=True)
    papel_no_projeto = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.membro} - {self.projeto} ({self.papel_no_projeto})"
    class Meta:
        verbose_name = "Projeto Membro"
        verbose_name_plural = "Projeto Membros"
        ordering = ["projeto", "membro"]