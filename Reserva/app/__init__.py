from flask import Blueprint, jsonify, request

bp = Blueprint('reservas', __name__)
reservas = []
reserva_id = 1

@bp.route('/reservas', methods=['POST'])
def criar_reserva():
    """
    Cria uma reserva
    ---
    tags:
      - Reservas
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            turma_id:
              type: integer
              example: 2
            data:
              type: string
              example: "2025-11-10"
    responses:
      201:
        description: Reserva criada
        schema:
          type: object
          properties:
            id:
              type: integer
            mensagem:
              type: string
    """
    global reserva_id
    data = request.json
    r = {"id": reserva_id, "turma_id": data["turma_id"], "data": data["data"]}
    reservas.append(r)
    reserva_id += 1
    return jsonify({"id": r["id"], "mensagem": "Reserva criada"}), 201

@bp.route('/reservas', methods=['GET'])
def listar_reservas():
    """
    Lista todas as reservas (opcional filtro por turma_id, data)
    ---
    tags:
      - Reservas
    parameters:
      - name: turma_id
        in: query
        type: integer
        required: false
      - name: data
        in: query
        type: string
        required: false
    responses:
      200:
        description: Lista de reservas
    """
    turma_id = request.args.get("turma_id", type=int)
    data = request.args.get("data")
    lista = reservas
    if turma_id:
        lista = [r for r in lista if r["turma_id"] == turma_id]
    if data:
        lista = [r for r in lista if r["data"] == data]
    return jsonify(lista), 200

@bp.route('/reservas/<int:id>', methods=['GET'])
def obter_reserva(id):
    """
    Busca reserva por id
    ---
    tags:
      - Reservas
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Reserva encontrada
      404:
        description: Não encontrada
    """
    r = next((x for x in reservas if x["id"] == id), None)
    return (jsonify(r), 200) if r else (jsonify({"erro": "Não encontrada"}), 404)

@bp.route('/reservas/<int:id>', methods=['PUT'])
def atualizar_reserva(id):
    """
    Atualiza reserva por id
    ---
    tags:
      - Reservas
    parameters:
      - name: id
        in: path
        type: integer
        required: true
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            turma_id:
              type: integer
            data:
              type: string
    responses:
      200:
        description: Reserva atualizada
      404:
        description: Não encontrada
    """
    data = request.json
    for reserva in reservas:
        if reserva["id"] == id:
            reserva["turma_id"] = data.get("turma_id", reserva["turma_id"])
            reserva["data"] = data.get("data", reserva["data"])
            return jsonify({"mensagem": "Atualizada"}), 200
    return jsonify({"erro": "Não encontrada"}), 404

@bp.route('/reservas/<int:id>', methods=['DELETE'])
def remover_reserva(id):
    """
    Remove reserva por id
    ---
    tags:
      - Reservas
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      204:
        description: Removida com sucesso
      404:
        description: Não encontrada
    """
    global reservas
    novo = [x for x in reservas if x["id"] != id]
    if len(novo) == len(reservas):
        return jsonify({"erro": "Não encontrada"}), 404
    reservas = novo
    return '', 204