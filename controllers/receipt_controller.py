from flask import Blueprint, request, jsonify
from services.receipt_service import process_receipt_service, get_points_service, get_receipt_service
from utils.validate_receipt import validate_receipt

receipt_bp = Blueprint("receipts", __name__)


@receipt_bp.route("/receipts/process", methods=["POST"])
def process_receipt():
    try:
        user_id = request.args.get("user_id")
        if user_id is None:
            return jsonify({"error": "user_id is required as a query parameter."}), 400

        receipt_data = request.get_json()
        if receipt_data is None:  # Check if JSON was not provided
            return jsonify({"error": "Invalid request body: JSON is required."}), 400

    except Exception as e:
        return jsonify({"error": f"Invalid request body: {str(e)}"}), 400

    errors = validate_receipt(receipt=receipt_data)

    # If there are validation errors, return them in the response
    if errors:
        return jsonify({"errors": errors}), 400

    receipt_id = process_receipt_service(user_id=user_id, receipt_data=receipt_data)
    return jsonify({"user_id": user_id, "receipt_id": receipt_id}), 201


@receipt_bp.route("/receipts/<string:receipt_id>/points", methods=["GET"])
def get_points(receipt_id):
    try:
        points = get_points_service(receipt_id)
        return jsonify({"points": points}), 200
    except ValueError:
        return jsonify({"error": "Receipt ID not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@receipt_bp.route("/receipts/<string:receipt_id>", methods=["GET"])
def get_receipt(receipt_id):
    try:
        receipt = get_receipt_service(receipt_id)
        return jsonify({"receipt": receipt}), 200
    except ValueError:
        return jsonify({"error": "Receipt ID not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

