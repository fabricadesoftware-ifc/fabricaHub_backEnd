from django.contrib import admin

from fabricahub.models import Membro, Projeto, Usuario, LogAuditoria, Task, ProjetoMembro


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "email", "tipo_usuario", "is_active", "is_staff", "is_superuser", "last_login")
    # search_fields = ("username", "first_name", "last_name", "email")
    fieldsets = (
        ("Informações de Credenciais", {
            "fields": ("username", "password")
        }),
        ("Informações Pessoais", {
            "fields": ("first_name", "last_name", "email", "tipo_usuario")
        }),
        ("Permissões e Status", {
            "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")
        }),
        ("Datas Importantes", {
            "fields": ("last_login",)
        }), 
    )

@admin.register(Membro)
class MembroAdmin(admin.ModelAdmin):
    list_display = ("usuario", "curso", "semestre", "squad")
    search_fields = ("usuario__username", "usuario__first_name", "usuario__last_name", "curso")
    list_filter = ("squad", "semestre")


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ("nome", "status", "data_inicio", "prazo_entrega")
    search_fields = ("nome",)
    list_filter = ("status",)


@admin.register(LogAuditoria)
class LogAuditoriaAdmin(admin.ModelAdmin):
    list_display = ("operador", "acao", "entidade_afetada", "created_at")
    search_fields = ("operador__username", "acao", "entidade_afetada")

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("titulo", "descricao", "status", "projeto", "responsavel")
    search_fields = ("titulo", "descricao")
    #
@admin.register(ProjetoMembro)
class ProjetoMembroAdmin(admin.ModelAdmin):
    list_display = ("projeto", "membro", "data_entrada", "data_saida")
    search_fields = ("projeto__nome", "membro__usuario__username")