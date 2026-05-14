from django.contrib import admin
from fabricahub.models import Usuario
# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'tipo_usuario')
    search_fields = ('username', 'email', 'first_name', 'tipo_usuario')
    list_filter = ('is_staff', 'is_active')
