from flask import Blueprint, jsonify
from .Controllers import ReservaController

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    """
    Verifica se a API está ativa.
    ---
    tags:
      - Status
    responses:
      200:
        description: API funcionando
    """
    return jsonify({"message": "API funcionando!"})

@bp.route('/reservas', methods=['GET'])
def get_all_reserva():
    """
    Lista todas as reservas.
    ---
    tags:
      - Reservas
    responses:
      200:
        description: Lista de reservas retornada
    """
    return ReservaController.get_all_reserva()

@bp.route('/reservas/<int:id>', methods=['GET'])
def get_reserva_by_id(id):
    """
    Busca uma reserva pelo ID.
    ---
    tags:
      - Reservas
    parameters:
      - in: path
        name: id
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Reserva encontrada
      404:
        description: Reserva não encontrada
    """
    return ReservaController.get_reserva_by_id(id)

@bp.route('/reservas', methods=['POST'])
def create_reserva():
    """
    Cria uma nova reserva.
    ---
    tags:
      - Reservas
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              num_sala:
                type: integer
              lab:
                type: boolean
              data:
                type: string
              turma_id:
                type: integer
    responses:
      201:
        description: Reserva criada
      400:
        description: Dados inválidos
    """
    return ReservaController.create_Reserva()

@bp.route('/reservas/<int:id>', methods=['PUT'])
def update_reserva(id):
    """
    Atualiza uma reserva.
    ---
    tags:
      - Reservas
    parameters:
      - in: path
        name: id
        required: true
        schema:
          type: integer
    requestBody:
      content:
        application/json:
          schema:
            type: object
    responses:
      200:
        description: Reserva atualizada
      404:
        description: Reserva não encontrada
    """
    return ReservaController.update_Reserva(id)

@bp.route('/reservas/<int:id>', methods=['DELETE'])
def delete_reserva(id):
    """
    Remove uma reserva.
    ---
    tags:
      - Reservas
    parameters:
      - in: path
        name: id
        required: true
        schema:
          type: integer
    responses:
      204:
        description: Reserva removida
      404:
        description: Reserva não encontrada
    """
    return ReservaController.delete_Reserva(id)
