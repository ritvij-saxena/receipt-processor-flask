import unittest
from app import app  # Import the main app


class ReceiptTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()  # Create a test client
        self.app.testing = True  # Enable testing mode

    def test_process_receipt_success(self):
        receipt_data = {
            "retailer": "CVS",
            "purchaseDate": "2022-06-25",
            "purchaseTime": "08:30",
            "items": [
                {"shortDescription": "Toothpaste", "price": "2.99"},
                {"shortDescription": "Shampoo", "price": "5.49"},
                {"shortDescription": "Conditioner", "price": "5.49"},
            ],
            "total": "13.97",
        }

        response = self.app.post("/receipts/process", json=receipt_data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.get_json())

    def test_process_receipt_validation_error(self):
        receipt_data = {
            "retailer": "CVS",
            "purchaseDate": "2022-06-25",
            "purchaseTime": "08:30",
            "items": [
                {"shortDescription": "Toothpaste"},  # Missing price
            ],
            "total": "13.97",
        }

        response = self.app.post("/receipts/process", json=receipt_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn("errors", response.get_json())

    def test_get_points_success(self):
        receipt_data = {
            "retailer": "CVS",
            "purchaseDate": "2022-06-25",
            "purchaseTime": "08:30",
            "items": [
                {"shortDescription": "Toothpaste", "price": "2.99"},
                {"shortDescription": "Shampoo", "price": "5.49"},
                {"shortDescription": "Conditioner", "price": "5.49"},
            ],
            "total": "13.97",
        }

        post_response = self.app.post("/receipts/process", json=receipt_data)
        receipt_id = post_response.get_json()["id"]

        points_response = self.app.get(f"/receipts/{receipt_id}/points")
        self.assertEqual(points_response.status_code, 200)
        self.assertIn("points", points_response.get_json())

    def test_get_points_not_found(self):
        response = self.app.get("/receipts/non-existent-id/points")
        self.assertEqual(response.status_code, 404)
        self.assertIn("error", response.get_json())


if __name__ == "__main__":
    unittest.main()
