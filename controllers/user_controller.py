from flask import Blueprint, request, jsonify

from models.user_model import User
from services.user_service import add_user_service, get_user_service
from utils.validate_user import validate_user

user_bp = Blueprint("users", __name__)

@user_bp.route("/users/adduser", methods=["POST"])
def add_user():
    try:
        user = request.get_json()
        if user is None:  # Check if JSON was not provided
            return jsonify({"error": "Invalid request body: JSON is required."}), 400

    except Exception as e:
        return jsonify({"error": f"Invalid request body: {str(e)}"}), 400

    errors = validate_user(user=user)

    # If there are validation errors, return them in the response
    if errors:
        return jsonify({"errors": errors}), 400
    current_user = add_user_service(user)
    return jsonify({"message": "user added successfully",
                    "user_id": current_user.id}), 201

@user_bp.route("/users/getuser/<string:user_id>", methods=["GET"])
def get_user(user_id):
    try:
        user: User = get_user_service(user_id)
        return jsonify({"user": user.to_dict()}), 200
    except ValueError:
        return jsonify({"error": "user not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500