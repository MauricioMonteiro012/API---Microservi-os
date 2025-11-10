from flask import request, jsonify
from .models import Atividades, Notas, db
import datetime

class AtividadesController:

    @staticmethod
    def get_all_atividades():
        atividades = Atividades.query.all()
        return jsonify([a.to_json() for a in atividades]), 200

    @staticmethod
    def get_atividade_by_id(id):
        atividade = Atividades.query.get(id)
        if not atividade:
            return jsonify({'message': 'Atividade não encontrada'}), 404
        return jsonify(atividade.to_json()), 200

    @staticmethod
    def create_Atividade():
        data = request.json
        if not data:
            return jsonify({'message': 'JSON inválido'}), 400
        
        nome_atividade = data.get('nome_atividade')
        peso_porcento = data.get('peso_porcento')
        turma_id = data.get('turma_id')
        professor_id = data.get('professor_id')
        data_entrega_str = data.get('data_entrega')
        
        if not nome_atividade or peso_porcento is None or not turma_id or not professor_id or not data_entrega_str:
            return jsonify({'message': 'Campos obrigatórios ausentes'}), 400
        
        try:
            data_entrega = datetime.date.fromisoformat(data_entrega_str)
        except ValueError:
            return jsonify({'message': 'Formato de data inválido (use YYYY-MM-DD)'}), 400

        nova_atividade = Atividades(
            nome_atividade=nome_atividade,
            descricao=data.get('descricao'),
            peso_porcento=peso_porcento,
            data_entrega=data_entrega,
            turma_id=turma_id,
            professor_id=professor_id
        )
        db.session.add(nova_atividade)
        db.session.commit()
        return jsonify(nova_atividade.to_json()), 201

    @staticmethod
    def update_atividade(id):
        atividade = Atividades.query.get(id)
        if not atividade:
            return jsonify({'message': 'Atividade não encontrada'}), 404
        
        data = request.json

        if 'data_entrega' in data:
            try:
                atividade.data_entrega = datetime.date.fromisoformat(data['data_entrega'])
            except ValueError:
                return jsonify({'message': 'Formato de data inválido (use YYYY-MM-DD)'}), 400

        atividade.nome_atividade = data.get('nome_atividade', atividade.nome_atividade)
        atividade.descricao = data.get('descricao', atividade.descricao)
        atividade.turma_id = data.get('turma_id', atividade.turma_id)
        atividade.professor_id = data.get('professor_id', atividade.professor_id)
        
        db.session.commit()
        return jsonify(atividade.to_json()), 200

    @staticmethod
    def delete_atividade(id):
        atividade = Atividades.query.get(id)
        if not atividade:
            return jsonify({'message': 'Atividade não encontrada'}), 404
        
        db.session.delete(atividade)
        db.session.commit()
        return '', 204


class NotasController:

    @staticmethod
    def get_all_notas():
        notas = Notas.query.all()
        return jsonify([n.to_json() for n in notas]), 200

    @staticmethod
    def get_notas_by_id(id):
        nota = Notas.query.get(id)
        if not nota:
            return jsonify({'message': 'Nota não encontrada'}), 404
        return jsonify(nota.to_json()), 200

    @staticmethod
    def create_Notas():
        data = request.json
        aluno_id = data.get('aluno_id')
        atividade_id = data.get('atividade_id')

        if not aluno_id or not atividade_id:
            return jsonify({'message': 'aluno_id e atividade_id são obrigatórios'}), 400

        nova_nota = Notas(
            nota=data.get('nota'),
            atividade_id=atividade_id,
            aluno_id=aluno_id
        )
        db.session.add(nova_nota)
        db.session.commit()
        return jsonify(nova_nota.to_json()), 201

    @staticmethod
    def update_Notas(id):
        nota = Notas.query.get(id)
        if not nota:
            return jsonify({'message': 'Nota não encontrada'}), 404
        
        data = request.json
        nota.nota = data.get('nota', nota.nota)
        nota.atividade_id = data.get('atividade_id', nota.atividade_id)
        nota.aluno_id = data.get('aluno_id', nota.aluno_id)

        db.session.commit()
        return jsonify(nota.to_json()), 200

    @staticmethod
    def delete_Notas(id):
        nota = Notas.query.get(id)
        if not nota:
            return jsonify({'message': 'Nota não encontrada'}), 404
        
        db.session.delete(nota)
        db.session.commit()
        return '', 204
