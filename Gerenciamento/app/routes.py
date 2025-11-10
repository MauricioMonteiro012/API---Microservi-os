from flask import Blueprint
from flasgger import swag_from
from .controllers import AlunoController, ProfessorController, TurmaController

bp = Blueprint('main', __name__)


@bp.get('/')
def index():
    """
    Verifica se a API está ativa
    ---
    tags:
      - Status
    responses:
      200:
        description: API funcionando
    """
    return {"message": "API funcionando!"}


@bp.get('/alunos')
def get_all_aluno():
    """
    Lista todos os alunos
    ---
    tags:
      - Alunos
    responses:
      200:
        description: Lista retornada com sucesso
    """
    return AlunoController.get_all_aluno()


@bp.get('/alunos/<int:id>')
def get_aluno_id(id):
    """
    Busca um aluno pelo ID
    ---
    tags:
      - Alunos
    parameters:
      - in: path
        name: id
        schema:
          type: integer
    responses:
      200:
        description: Aluno encontrado
      404:
        description: Aluno não encontrado
    """
    return AlunoController.get_aluno_by_id(id)


@bp.post('/alunos')
def create_aluno():
    """
    Cria um novo aluno
    ---
    tags:
      - Alunos
    requestBody:
      required: True
      content:
        application/json:
          example:
            nome: João
            idade: 18
    responses:
      201:
        description: Aluno criado
    """
    return AlunoController.create_Aluno()


@bp.put('/alunos/<int:id>')
def update_aluno(id):
    """
    Atualiza um aluno pelo ID
    ---
    tags:
      - Alunos
    parameters:
      - in: path
        name: id
        schema:
          type: integer
    responses:
      200:
        description: Atualizado com sucesso
      404:
        description: Aluno não encontrado
    """
    return AlunoController.update_Aluno(id)


@bp.delete('/alunos/<int:id>')
def delete_aluno(id):
    """
    Remove um aluno pelo ID
    ---
    tags:
      - Alunos
    parameters:
      - in: path
        name: id
        schema:
          type: integer
    responses:
      200:
        description: Removido com sucesso
      404:
        description: Aluno não encontrado
    """
    return AlunoController.delete_Aluno(id)


@bp.get('/professores')
def get_all_professor():
    """
    Lista todos os professores
    ---
    tags:
      - Professores
    responses:
      200:
        description: Lista retornada com sucesso
    """
    return ProfessorController.get_all_professor()


@bp.get('/professores/<int:id>')
def get_professor_id(id):
    """
    Busca um professor pelo ID
    ---
    tags:
      - Professores
    parameters:
      - in: path
        name: id
        schema:
          type: integer
    """
    return ProfessorController.get_professor_by_id(id)


@bp.post('/professores')
def create_professor():
    """
    Cria um novo professor
    ---
    tags:
      - Professores
    requestBody:
      required: True
      content:
        application/json:
          example:
            nome: Maria
            especialidade: Matemática
    """
    return ProfessorController.create_Professor()


@bp.put('/professores/<int:id>')
def update_professor(id):
    """
    Atualiza um professor pelo ID
    ---
    tags:
      - Professores
    """
    return ProfessorController.update_Professor(id)


@bp.delete('/professores/<int:id>')
def delete_professor(id):
    """
    Remove um professor pelo ID
    ---
    tags:
      - Professores
    """
    return ProfessorController.delete_Professor(id)


@bp.get('/turmas')
def get_all_turma():
    """
    Lista todas as turmas
    ---
    tags:
      - Turmas
    """
    return TurmaController.get_all_turma()


@bp.get('/turmas/<int:id>')
def get_turma_id(id):
    """
    Busca uma turma pelo ID
    ---
    tags:
      - Turmas
    """
    return TurmaController.get_turma_by_id(id)


@bp.post('/turmas')
def create_turma():
    """
    Cria uma nova turma
    ---
    tags:
      - Turmas
    requestBody:
      required: True
      content:
        application/json:
          example:
            nome: Turma A
            ano: 2024
    """
    return TurmaController.create_Turma()


@bp.put('/turmas/<int:id>')
def update_turma(id):
    """
    Atualiza uma turma pelo ID
    ---
    tags:
      - Turmas
    """
    return TurmaController.update_Turma(id)


@bp.delete('/turmas/<int:id>')
def delete_turma(id):
    """
    Remove uma turma pelo ID
    ---
    tags:
      - Turmas
    """
    return TurmaController.delete_Turma(id)
