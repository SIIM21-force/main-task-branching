import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_root_endpoint(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["status"], "operational")

    def test_health_endpoint(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["status"], "healthy")

    def test_system_endpoint(self):
        response = self.client.get("/system")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("operating_system", data)

if __name__ == "__main__":
    unittest.main()
