from .atualizar import atualizar_aluno
from .buscar_id import buscar_por_id
from .buscar_matricula import buscar_por_matricula
from .cadastrar import cadastrar_aluno
from .deletar import deletar_aluno
from .desativar import desativar_aluno
from .estatisticas import exibir_estatisticas
from .listar import listar_alunos
from .listar_curso import listar_por_curso

__all__ = [
    "atualizar_aluno",
    "buscar_por_id",
    "buscar_por_matricula",
    "cadastrar_aluno",
    "deletar_aluno",
    "desativar_aluno",
    "exibir_estatisticas",
    "listar_alunos",
    "listar_por_curso",
]
