from math import ceil


def calculate_points(receipt):
    points = 0

    # 1. Points for retailer name
    retailer_name = receipt.get("retailer", "")
    points += sum(c.isalnum() for c in retailer_name)

    # 2. 50 points if total is a round dollar amount with no cents
    total = float(receipt.get("total", 0))
    if total.is_integer():
        points += 50

    # 3. 25 points if total is a multiple of 0.25
    if total % 0.25 == 0:
        points += 25

    # 4. 5 points for every two items
    items = receipt.get("items", [])
    points += (len(items) // 2) * 5

    # 5. Points for item description
    for item in items:
        description = item.get("shortDescription", "").strip()
        price = float(item.get("price", 0))
        if len(description) % 3 == 0:
            points += ceil(price * 0.2)

    # 6. 6 points if the day in the purchase date is odd
    purchase_date = receipt.get("purchaseDate", "")
    day = int(purchase_date.split("-")[2]) if purchase_date else 0
    if day % 2 != 0:
        points += 6

    # 7. 10 points if the time is between 2:00pm and 4:00pm
    purchase_time = receipt.get("purchaseTime", "00:00")
    hour = int(purchase_time.split(":")[0])
    if 14 <= hour < 16:
        points += 10

    return points
