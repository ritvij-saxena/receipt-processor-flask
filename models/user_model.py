import uuid

class User:
    def __init__(self, first_name, last_name):
        self.id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.total_receipts_submitted = 0

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "total_receipts_submitted": self.total_receipts_submitted
        }