from flask import request, jsonify
from .models import Reserva, db
import datetime

class ReservaController:

    @staticmethod
    def get_all_reserva():
        reservas = Reserva.query.all()
        return jsonify([r.to_json() for r in reservas]), 200
    
    @staticmethod
    def get_reserva_by_id(id):
        reserva = Reserva.query.get(id)
        if not reserva:
            return jsonify({'message': 'Reserva não encontrada'}), 404
        return jsonify(reserva.to_json()), 200
    
    @staticmethod
    def create_Reserva():
        data = request.json
        turma_id = data.get('turma_id')
        if not turma_id:
            return jsonify({'message': 'turma_id é obrigatório'}), 400

        data_value = data.get('data')
        if isinstance(data_value, str):
            try:
                data_value = datetime.date.fromisoformat(data_value)
            except ValueError:
                return jsonify({'message': 'Data inválida. Use YYYY-MM-DD'}), 400

        nova_reserva = Reserva(
            num_sala=data.get('num_sala'),
            lab=data.get('lab'),
            data=data_value,
            turma_id=turma_id
        )
        db.session.add(nova_reserva)
        db.session.commit()
        return jsonify(nova_reserva.to_json()), 201
    
    @staticmethod
    def update_Reserva(id):
        reserva = Reserva.query.get(id)
        if not reserva:
            return jsonify({'message': 'Reserva não encontrada'}), 404
        
        data = request.json
        reserva.num_sala = data.get('num_sala', reserva.num_sala)
        reserva.lab = data.get('lab', reserva.lab)

        new_data = data.get('data', reserva.data)
        if isinstance(new_data, str):
            try:
                new_data = datetime.date.fromisoformat(new_data)
            except ValueError:
                return jsonify({'message': 'Data inválida. Use YYYY-MM-DD'}), 400
        reserva.data = new_data
        
        reserva.turma_id = data.get('turma_id', reserva.turma_id)

        db.session.commit()
        return jsonify(reserva.to_json()), 200
    
    @staticmethod
    def delete_Reserva(id):
        reserva = Reserva.query.get(id)
        if not reserva:
            return jsonify({'message': 'Reserva não encontrada'}), 404
        
        db.session.delete(reserva)
        db.session.commit()
        return '', 204
