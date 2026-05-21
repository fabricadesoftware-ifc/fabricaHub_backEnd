from .membro import MembroSerializer
from .projeto import ProjetoSerializer
from .usuario import UsuarioSerializer
from .log_auditoria import LogAuditoriaSerializer
from .task import TaskSerializer
__all__ = [
    "UsuarioSerializer",
    "MembroSerializer",
    "ProjetoSerializer",
    "LogAuditoriaSerializer",   
    "TaskSerializer"
]