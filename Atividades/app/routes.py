from flask import Blueprint, jsonify, request
from .Controllers import AtividadesController, NotasController

bp = Blueprint('api', __name__)


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
    return jsonify({"message": "API funcionando!"}), 200


# ATIVIDADES
@bp.get('/atividades')
def listar_atividades():
    """
    Lista todas as atividades
    ---
    tags:
      - Atividades
    responses:
      200:
        description: Lista retornada
    """
    return AtividadesController.get_all_atividades()


@bp.get('/atividades/<int:id>')
def obter_atividade(id):
    """
    Busca uma atividade pelo ID
    ---
    tags:
      - Atividades
    parameters:
      - in: path
        name: id
        schema:
          type: integer
    responses:
      200:
        description: Atividade encontrada
      404:
        description: Não encontrada
    """
    return AtividadesController.get_atividade_by_id(id)


@bp.post('/atividades')
def criar_atividade():
    """
    Cria uma nova atividade
    ---
    tags:
      - Atividades
    requestBody:
      required: true
      content:
        application/json:
          example:
            titulo: Exercício 1
            descricao: Responder questões de matemática
            professor_id: 1
            turma_id: 2
    responses:
      201:
        description: Criado com sucesso
    """
    return AtividadesController.create_Atividade(request.json)


@bp.put('/atividades/<int:id>')
def atualizar_atividade(id):
    """
    Atualiza uma atividade pelo ID
    ---
    tags:
      - Atividades
    parameters:
      - in: path
        name: id
        schema:
          type: integer
    responses:
      200:
        description: Atualizada com sucesso
      404:
        description: Não encontrada
    """
    return AtividadesController.update_atividade(id, request.json)


@bp.delete('/atividades/<int:id>')
def remover_atividade(id):
    """
    Remove uma atividade pelo ID
    ---
    tags:
      - Atividades
    responses:
      200:
        description: Removida com sucesso
      404:
        description: Não encontrada
    """
    return AtividadesController.delete_atividade(id)


# NOTAS
@bp.get('/notas')
def listar_notas():
    """
    Lista todas as notas
    ---
    tags:
      - Notas
    responses:
      200:
        description: Lista retornada
    """
    return NotasController.get_all_notas()


@bp.get('/notas/<int:id>')
def obter_nota(id):
    """
    Busca uma nota pelo ID
    ---
    tags:
      - Notas
    parameters:
      - in: path
        name: id
        schema:
          type: integer
    responses:
      200:
        description: Nota encontrada
      404:
        description: Não encontrada
    """
    return NotasController.get_notas_by_id(id)


@bp.post('/notas')
def criar_nota():
    """
    Cria uma nova nota
    ---
    tags:
      - Notas
    requestBody:
      required: true
      content:
        application/json:
          example:
            aluno_id: 1
            atividade_id: 3
            nota: 9.5
    responses:
      201:
        description: Criado com sucesso
    """
    return NotasController.create_Notas(request.json)


@bp.put('/notas/<int:id>')
def atualizar_nota(id):
    """
    Atualiza uma nota pelo ID
    ---
    tags:
      - Notas
    responses:
      200:
        description: Atualizada com sucesso
      404:
        description: Não encontrada
    """
    return NotasController.update_Notas(id, request.json)


@bp.delete('/notas/<int:id>')
def remover_nota(id):
    """
    Remove uma nota pelo ID
    ---
    tags:
      - Notas
    responses:
      200:
        description: Removida com sucesso
      404:
        description: Não encontrada
    """
    return NotasController.delete_Notas(id)
