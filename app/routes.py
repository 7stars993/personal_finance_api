from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import db, Transaction

finance_bp = Blueprint('finance', __name__)

# Route untuk root
@finance_bp.route('/', methods=['GET'])
def home():
    return "API Catatan Keuangan Pribadi Aktif!"

@finance_bp.route('/transactions', methods=['POST'])
@jwt_required()
def add_transaction():
    data = request.get_json()
    user_id = get_jwt_identity()
    new_tx = Transaction(
        amount=data['amount'],
        type=data['type'],
        description=data.get('description', ''),
        user_id=user_id
    )
    db.session.add(new_tx)
    db.session.commit()
    return jsonify(message="Transaction added"), 201

@finance_bp.route('/transactions', methods=['GET'])
@jwt_required()
def get_transactions():
    user_id = get_jwt_identity()
    txs = Transaction.query.filter_by(user_id=user_id).all()
    result = [{
        "id": t.id,
        "amount": t.amount,
        "type": t.type,
        "description": t.description
    } for t in txs]
    return jsonify(result), 200
