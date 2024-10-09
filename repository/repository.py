from collections import defaultdict
import threading


# In-memory store for receipts and points
class ReceiptRepository:
    def __init__(self):
        self.receipts = defaultdict(dict)  # Stores receipts
        self.points = defaultdict(int)  # Stores points awarded
        self.lock = threading.Lock()  # For thread-safe operations

    def add_receipt(self, receipt_id, receipt_data):
        with self.lock:
            self.receipts[receipt_id] = receipt_data

    def get_receipt(self, receipt_id):
        return self.receipts.get(receipt_id)

    def add_points(self, receipt_id, points):
        with self.lock:
            self.points[receipt_id] = points

    def get_points(self, receipt_id):
        return self.points.get(receipt_id, 0)


# Singleton instance of ReceiptRepository
repository = ReceiptRepository()
