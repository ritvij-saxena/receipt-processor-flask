POINTS_FOR_NEW_USER = {
    0: 1000,
    1: 500,
    2: 250
}

def get_points_for_new_users(total_receipts_submitted):
    if not isinstance(total_receipts_submitted, int):
        raise Exception("Wrong type")
    return POINTS_FOR_NEW_USER.get(total_receipts_submitted,0)