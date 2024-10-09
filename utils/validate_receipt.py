def validate_receipt(receipt):
    errors = []

    if not isinstance(receipt, dict):
        errors.append("Receipt must be a JSON object.")

    required_fields = ["retailer", "purchaseDate", "purchaseTime", "items", "total"]

    for field in required_fields:
        if field not in receipt:
            errors.append(f"Missing required field: {field}")

    if not isinstance(receipt.get("items", []), list) or len(receipt["items"]) == 0:
        errors.append("Items must be a non-empty list.")

    for item in receipt.get("items", []):
        if "shortDescription" not in item or "price" not in item:
            errors.append("Each item must have 'shortDescription' and 'price' fields.")
            continue
        try:
            float(item["price"])  # Ensure price is a valid number
        except ValueError:
            errors.append(
                f"Invalid price for item: {item.get('shortDescription', 'unknown')}"
            )
        except KeyError:
            print(f"Field is missing. Actual fields are {item.keys()}")
            errors.append(f"Field is missing. Actual fields are {item.keys()}")

    return errors
