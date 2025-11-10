from flask import Blueprint, jsonify, request

bp = Blueprint('gerenciamento', __name__)

professores = []
turmas = []
alunos = []
professor_id = 1
turma_id = 1
aluno_id = 1

# ----------- PROFESSORES -------------

@bp.route('/professores', methods=['POST'])
def criar_professor():
    """
    Cadastra um novo professor
    ---
    tags:
      - Gerenciamento
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            nome:
              type: string
              example: "Maria"
            disciplina:
              type: string
              example: "Matemática"
    responses:
      201:
        description: Professor criado
        schema:
          type: object
          properties:
            id:
              type: integer
            mensagem:
              type: string
    """
    global professor_id
    data = request.json
    p = {"id": professor_id, "nome": data["nome"], "disciplina": data["disciplina"]}
    professores.append(p)
    professor_id += 1
    return jsonify({"id": p["id"], "mensagem": "Professor criado"}), 201

@bp.route('/professores', methods=['GET'])
def listar_professores():
    """
    Lista todos os professores (opcional filtro por nome ou disciplina)
    ---
    tags:
      - Gerenciamento
    parameters:
      - name: nome
        in: query
        type: string
        required: false
      - name: disciplina
        in: query
        type: string
        required: false
    responses:
      200:
        description: Lista de professores
    """
    nome = request.args.get("nome")
    disciplina = request.args.get("disciplina")
    lista = professores
    if nome:
        lista = [p for p in lista if nome.lower() in p["nome"].lower()]
    if disciplina:
        lista = [p for p in lista if disciplina.lower() in p["disciplina"].lower()]
    return jsonify(lista), 200

@bp.route('/professores/<int:id>', methods=['GET'])
def obter_professor(id):
    """
    Busca professor pelo id
    ---
    tags:
      - Gerenciamento
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200: {description: Encontrado}
      404: {description: Não encontrado}
    """
    p = next((x for x in professores if x["id"] == id), None)
    return (jsonify(p), 200) if p else (jsonify({"erro": "Não encontrado"}), 404)

@bp.route('/professores/<int:id>', methods=['PUT'])
def atualizar_professor(id):
    """
    Atualiza professor
    ---
    tags:
      - Gerenciamento
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
            nome:
              type: string
            disciplina:
              type: string
    responses:
      200: {description: Atualizado}
      404: {description: Não encontrado}
    """
    data = request.json
    for p in professores:
        if p["id"] == id:
            p.update(data)
            return jsonify({"mensagem": "Atualizado"}), 200
    return jsonify({"erro": "Não encontrado"}), 404

@bp.route('/professores/<int:id>', methods=['DELETE'])
def remover_professor(id):
    """
    Remove professor
    ---
    tags:
      - Gerenciamento
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      204: {description: Removido}
      404: {description: Não encontrado}
    """
    global professores
    novo = [x for x in professores if x["id"] != id]
    if len(novo) == len(professores):
        return jsonify({"erro": "Não encontrado"}), 404
    professores = novo
    return '', 204

# ----------- TURMAS -------------

@bp.route('/turmas', methods=['POST'])
def criar_turma():
    """
    Cadastra uma turma
    ---
    tags:
      - Gerenciamento
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            nome:
              type: string
              example: "Turma A"
    responses:
      201:
        description: Turma criada
        schema:
          type: object
          properties:
            id:
              type: integer
            mensagem:
              type: string
    """
    global turma_id
    data = request.json
    t = {"id": turma_id, "nome": data["nome"]}
    turmas.append(t)
    turma_id += 1
    return jsonify({"id": t["id"], "mensagem": "Turma criada"}), 201

@bp.route('/turmas', methods=['GET'])
def listar_turmas():
    """
    Lista turmas (opcional: filtro por nome)
    ---
    tags:
      - Gerenciamento
    parameters:
      - name: nome
        in: query
        type: string
        required: false
    responses:
      200:
        description: Lista de turmas
    """
    nome = request.args.get("nome")
    lista = turmas
    if nome:
        lista = [t for t in lista if nome.lower() in t["nome"].lower()]
    return jsonify(lista), 200

@bp.route('/turmas/<int:id>', methods=['GET'])
def obter_turma(id):
    """
    Busca turma pelo id
    ---
    tags:
      - Gerenciamento
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200: {description: Encontrado}
      404: {description: Não encontrado}
    """
    t = next((x for x in turmas if x["id"] == id), None)
    return (jsonify(t), 200) if t else (jsonify({"erro": "Não encontrado"}), 404)

@bp.route('/turmas/<int:id>', methods=['PUT'])
def atualizar_turma(id):
    """
    Atualiza turma
    ---
    tags:
      - Gerenciamento
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
            nome:
              type: string
    responses:
      200: {description: Atualizado}
      404: {description: Não encontrado}
    """
    data = request.json
    for t in turmas:
        if t["id"] == id:
            t.update(data)
            return jsonify({"mensagem": "Atualizado"}), 200
    return jsonify({"erro": "Não encontrado"}), 404

@bp.route('/turmas/<int:id>', methods=['DELETE'])
def remover_turma(id):
    """
    Remove turma
    ---
    tags:
      - Gerenciamento
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      204: {description: Removido}
      404: {description: Não encontrado}
    """
    global turmas
    novo = [x for x in turmas if x["id"] != id]
    if len(novo) == len(turmas):
        return jsonify({"erro": "Não encontrado"}), 404
    turmas = novo
    return '', 204

# ----------- ALUNOS -------------

@bp.route('/alunos', methods=['POST'])
def criar_aluno():
    """
    Cadastra um aluno
    ---
    tags:
      - Gerenciamento
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            nome:
              type: string
              example: "João"
    responses:
      201:
        description: Aluno criado
        schema:
          type: object
          properties:
            id:
              type: integer
            mensagem:
              type: string
    """
    global aluno_id
    data = request.json
    a = {"id": aluno_id, "nome": data["nome"]}
    alunos.append(a)
    aluno_id += 1
    return jsonify({"id": a["id"], "mensagem": "Aluno criado"}), 201

@bp.route('/alunos', methods=['GET'])
def listar_alunos():
    """
    Lista alunos (opcional: filtro por nome)
    ---
    tags:
      - Gerenciamento
    parameters:
      - name: nome
        in: query
        type: string
        required: false
    responses:
      200:
        description: Lista de alunos
    """
    nome = request.args.get("nome")
    lista = alunos
    if nome:
        lista = [a for a in lista if nome.lower() in a["nome"].lower()]
    return jsonify(lista), 200

@bp.route('/alunos/<int:id>', methods=['GET'])
def obter_aluno(id):
    """
    Busca aluno pelo id
    ---
    tags:
      - Gerenciamento
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200: {description: Encontrado}
      404: {description: Não encontrado}
    """
    a = next((x for x in alunos if x["id"] == id), None)
    return (jsonify(a), 200) if a else (jsonify({"erro": "Não encontrado"}), 404)

@bp.route('/alunos/<int:id>', methods=['PUT'])
def atualizar_aluno(id):
    """
    Atualiza aluno
    ---
    tags:
      - Gerenciamento
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
            nome:
              type: string
    responses:
      200: {description: Atualizado}
      404: {description: Não encontrado}
    """
    data = request.json
    for a in alunos:
        if a["id"] == id:
            a.update(data)
            return jsonify({"mensagem": "Atualizado"}), 200
    return jsonify({"erro": "Não encontrado"}), 404

@bp.route('/alunos/<int:id>', methods=['DELETE'])
def remover_aluno(id):
    """
    Remove aluno
    ---
    tags:
      - Gerenciamento
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      204: {description: Removido}
      404: {description: Não encontrado}
    """
    global alunos
    novo = [x for x in alunos if x["id"] != id]
    if len(novo) == len(alunos):
        return jsonify({"erro": "Não encontrado"}), 404
    alunos = novo
    return '', 204