from .membro import MembroViewSet
from .log_auditoria import LogAuditoriaViewSet
from .projeto import ProjetoViewSet
from .usuario import UsuarioViewSet
from .task import TaskViewSet
__all__ = [
    "UsuarioViewSet",
    "MembroViewSet",
    "ProjetoViewSet",
    "LogAuditoriaViewSet",
    "TaskViewSet",
]