def validate_user(user):
    errors = []

    if not isinstance(user, dict):
        errors.append("User must be a JSON object.")

    required_fields = ["first_name", "last_name"]

    for field in required_fields:
        if field not in user:
            errors.append(f"Missing required field: {field}")


    return errors
