from flask import Blueprint, jsonify, request

bp = Blueprint('atividades', __name__)
atividades, notas = [], []
atividade_id, nota_id = 1, 1

@bp.route('/atividades', methods=['POST'])
def criar_atividade():
    """
    Cria uma nova atividade
    ---
    tags:
      - Atividades
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            professor_id:
              type: integer
              example: 1
            turma_id:
              type: integer
              example: 2
            titulo:
              type: string
              example: "Prova"
            nota:
              type: number
              example: 7.5
    responses:
      201:
        description: Atividade criada
        schema:
          type: object
          properties:
            id:
              type: integer
            mensagem:
              type: string
    """
    global atividade_id
    data = request.json
    a = {
        "id": atividade_id,
        "professor_id": data["professor_id"],
        "turma_id": data["turma_id"],
        "titulo": data["titulo"],
        "nota": data["nota"]
    }
    atividades.append(a)
    atividade_id += 1
    return jsonify({"id": a["id"], "mensagem": "Atividade criada"}), 201

@bp.route('/atividades', methods=['GET'])
def listar_atividades():
    """
    Lista todas as atividades (opcional: filtro por professor_id, turma_id)
    ---
    tags:
      - Atividades
    parameters:
      - name: professor_id
        in: query
        type: integer
        required: false
        description: Filtro por professor
      - name: turma_id
        in: query
        type: integer
        required: false
        description: Filtro por turma
    responses:
      200:
        description: Lista
    """
    professor_id = request.args.get('professor_id', type=int)
    turma_id = request.args.get('turma_id', type=int)
    lista = atividades
    if professor_id:
        lista = [a for a in lista if a["professor_id"] == professor_id]
    if turma_id:
        lista = [a for a in lista if a["turma_id"] == turma_id]
    return jsonify(lista), 200

@bp.route('/atividades/<int:id>', methods=['GET'])
def obter_atividade(id):
    """
    Busca uma atividade pelo ID
    ---
    tags:
      - Atividades
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID da atividade
    responses:
      200:
        description: Atividade encontrada
      404:
        description: Não encontrada
    """
    a = next((x for x in atividades if x["id"] == id), None)
    return (jsonify(a), 200) if a else (jsonify({"erro": "Não encontrada"}), 404)

@bp.route('/atividades/<int:id>', methods=['PUT'])
def atualizar_atividade(id):
    """
    Atualiza uma atividade pelo ID
    ---
    tags:
      - Atividades
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
            professor_id:
              type: integer
            turma_id:
              type: integer
            titulo:
              type: string
            nota:
              type: number
    responses:
      200:
        description: Atualizada
      404:
        description: Não encontrada
    """
    data = request.json
    for a in atividades:
        if a["id"] == id:
            a.update(data)
            return jsonify({"mensagem": "Atualizada"}), 200
    return jsonify({"erro": "Não encontrada"}), 404

@bp.route('/atividades/<int:id>', methods=['DELETE'])
def remover_atividade(id):
    """
    Remove atividade pelo id
    ---
    tags:
      - Atividades
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      204:
        description: Removida
    """
    global atividades
    atividades = [a for a in atividades if a["id"] != id]
    return '', 204