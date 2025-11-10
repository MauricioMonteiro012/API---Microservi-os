from flask import Blueprint, jsonify, request

bp = Blueprint('atividades', __name__)

atividades = []
atividade_id = 1

@bp.route('/', methods=['GET'])
def status():
    return "API Atividades funcionando!"

@bp.route('', methods=['POST'])
def criar_atividade():
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

@bp.route('', methods=['GET'])
def listar_atividades():
    return jsonify(atividades), 200

@bp.route('/<int:id>', methods=['GET'])
def obter_atividade(id):
    a = next((x for x in atividades if x["id"] == id), None)
    return (jsonify(a), 200) if a else (jsonify({"erro": "Não encontrada"}), 404)