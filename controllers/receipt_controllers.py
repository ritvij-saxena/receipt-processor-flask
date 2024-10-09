from flask import Blueprint, request, jsonify
from services.receipt_service import process_receipt_service, get_points_service

receipt_bp = Blueprint("receipts", __name__)


@receipt_bp.route("/receipts/process", methods=["POST"])
def process_receipt():
    receipt_data = request.get_json()
    receipt_id = process_receipt_service(receipt_data)
    return jsonify({"id": receipt_id}), 200


@receipt_bp.route("/receipts/<receipt_id>/points", methods=["GET"])
def get_points(receipt_id):
    points = get_points_service(receipt_id)
    return jsonify({"points": points}), 200
