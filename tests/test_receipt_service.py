# tests/test_receipt_service.py

import unittest
from unittest.mock import patch
from services.receipt_service import get_points_service
from repository.repository import repository


class TestReceiptService(unittest.TestCase):

    def setUp(self):
        self.test_receipt_id = "test-id"
        self.test_points = 30
        # Add test data to repository
        repository.add_receipt(self.test_receipt_id, {"retailer": "Test Retailer"})
        repository.add_points(self.test_receipt_id, self.test_points)

    def test_get_points_success(self):
        points = get_points_service(self.test_receipt_id)
        self.assertEqual(points, self.test_points)

    def test_get_points_not_found(self):
        with self.assertRaises(ValueError):
            get_points_service("invalid-id")

    def tearDown(self):
        # Clear the repository after each test
        repository.receipts.clear()
        repository.points.clear()


if __name__ == "__main__":
    unittest.main()
