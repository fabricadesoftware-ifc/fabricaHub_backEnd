from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from fabricahub.models import Membro, PerformanceLog, Projeto, Usuario


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = ("id", "username", "first_name", "last_name", "email", "tipo_usuario")
    search_fields = ("username", "first_name", "last_name", "email")
    
    fieldsets = UserAdmin.fieldsets + (
        ('Configurações do FábricaHUB', {'fields': ('tipo_usuario',)}),
    )



@admin.register(Membro)
class MembroAdmin(admin.ModelAdmin):
    list_display = ("id", "usuario", "curso", "semestre", "squad")
    search_fields = ("usuario__username", "usuario__first_name", "usuario__last_name", "curso")
    list_filter = ("squad", "semestre")


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "status", "data_inicio", "prazo_entrega")
    search_fields = ("nome",)
    list_filter = ("status",)


@admin.register(PerformanceLog)
class PerformanceLogAdmin(admin.ModelAdmin):
    list_display = ("id", "membro", "projeto", "metrica_entrega", "created_at")
    search_fields = ("membro__usuario__username", "projeto__nome")