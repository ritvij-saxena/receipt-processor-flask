from collections import defaultdict
import threading

class UserReceiptMapper:
    def __init__(self):
        self.user_to_receipt_mapping = defaultdict()
        self.receipt_to_user_mapping = defaultdict()
        self.lock = threading.Lock()

    def add_mapping(self, receipt_id, user_id):
        with self.lock:
            self.user_to_receipt_mapping[user_id] = receipt_id
            self.receipt_to_user_mapping[receipt_id] = user_id

    def get_user_id_for_receipt_id(self, receipt_id):
        with self.lock:
            return self.receipt_to_user_mapping[receipt_id].copy()

    def get_receipt_id_for_user_id(self, user_id):
        with self.lock:
            return self.user_to_receipt_mapping[user_id].copy()

# Singleton instance of UserReceiptMapper
user_receipt_mapper = UserReceiptMapper()