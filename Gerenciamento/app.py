from flask import Blueprint, jsonify, request

bp = Blueprint('gerenciamento', __name__)

professores = []
professor_id = 1

@bp.route('/', methods=['GET'])
def status():
    return "API Gerenciamento funcionando!"

@bp.route('', methods=['POST'])
def criar_professor():
    global professor_id
    data = request.json
    p = {"id": professor_id, "nome": data["nome"], "disciplina": data["disciplina"]}
    professores.append(p)
    professor_id += 1
    return jsonify({"id": p["id"], "mensagem": "Professor criado"}), 201

@bp.route('', methods=['GET'])
def listar_professores():
    return jsonify(professores), 200

@bp.route('/<int:id>', methods=['GET'])
def obter_professor(id):
    p = next((x for x in professores if x["id"] == id), None)
    return (jsonify(p), 200) if p else (jsonify({"erro": "Não encontrado"}), 404)