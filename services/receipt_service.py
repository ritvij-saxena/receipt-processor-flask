import uuid
from repository.repository import repository
from utils.points_calculator import calculate_points
from concurrent.futures import ThreadPoolExecutor  # Importing ThreadPoolExecutor

# Thread pool executor for async processing
executor = ThreadPoolExecutor()  # Create a thread pool for executing async tasks


def process_receipt_service(receipt_data):
    receipt_id = str(uuid.uuid4())
    repository.add_receipt(receipt_id, receipt_data)

    # Submit the points calculation to the thread pool
    executor.submit(
        calculate_and_store_points, receipt_id, receipt_data
    )  # Submit the task

    return receipt_id


def calculate_and_store_points(receipt_id, receipt_data):
    points = calculate_points(receipt_data)
    repository.add_points(receipt_id, points)


def get_points_service(receipt_id):
    try:
        points = repository.get_points(receipt_id)
        return points
    except KeyError:
        raise ValueError("Receipt ID not found.")
