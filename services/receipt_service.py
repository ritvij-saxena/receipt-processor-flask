import uuid

from concurrent.futures import ThreadPoolExecutor  # Importing ThreadPoolExecutor
from models.user_model import User
from repository.user_repository import user_repository
from repository.receipt_repository import receipt_repository
from repository.user_receipt_mapper_repository import user_receipt_mapper
from utils.points_calculator import calculate_points
from utils.points_new_user import get_points_for_new_users

# Thread pool executor for async processing
executor = ThreadPoolExecutor()  # Create a thread pool for executing async tasks


def process_receipt_service(user_id, receipt_data):
    receipt_id = str(uuid.uuid4())
    receipt_repository.add_receipt(receipt_id, receipt_data)

    # storing user_id to receipt_id and vice-versa
    user_receipt_mapper.add_mapping(receipt_id=receipt_id, user_id=user_id)

    # Submit the points calculation to the thread pool
    executor.submit(
        calculate_and_store_points, user_id, receipt_id, receipt_data
    )  # Submit the task

    return receipt_id


def calculate_and_store_points(user_id,receipt_id,receipt_data):
    points = calculate_points(receipt_data)
    points += calculate_points_for_new_users(user_id) # Add points for new users

    receipt_repository.add_points(receipt_id, points)

    current_user:User = user_repository.get_user(user_id)
    current_user.total_receipts_submitted += 1

    user_repository.add_or_update_user(current_user)

def get_points_service(receipt_id):
    try:
        points = receipt_repository.get_points(receipt_id)
        return points
    except KeyError:
        raise ValueError("Receipt ID not found.")

def get_receipt_service(receipt_id):
    try:
        receipt = receipt_repository.get_receipt(receipt_id)
        points = receipt_repository.get_points(receipt_id)
        return receipt | {"points": points}
    except KeyError:
        raise ValueError("Receipt ID not found.")

def calculate_points_for_new_users(user_id):
    points = 0
    current_user: User = user_repository.get_user(user_id)
    points += get_points_for_new_users(current_user.total_receipts_submitted)
    return points
