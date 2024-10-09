from flask import Blueprint, request, jsonify
from services.receipt_service import process_receipt_service, get_points_service
from utils.validate_receipt import validate_receipt

receipt_bp = Blueprint("receipts", __name__)


@receipt_bp.route("/receipts/process", methods=["POST"])
def process_receipt():
    receipt_data = request.get_json()
    errors = validate_receipt(receipt=receipt_data)

    # If there are validation errors, return them in the response
    if errors:
        return jsonify({"errors": errors}), 400

    receipt_id = process_receipt_service(receipt_data)
    return jsonify({"id": receipt_id}), 201


@receipt_bp.route("/receipts/<receipt_id>/points", methods=["GET"])
def get_points(receipt_id):
    points = get_points_service(receipt_id)
    return jsonify({"points": points}), 200
