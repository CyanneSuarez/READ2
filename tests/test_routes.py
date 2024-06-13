import unittest
from flask import Flask
from flask_testing import TestCase
from READ2 import create_app, db
from READ2.models import Product

class TestProductRoutes(TestCase):

    def create_app(self):
        app = create_app('testing')  # Ensure you have a testing configuration
        return app

    def setUp(self):
        db.create_all()
        self.product = Product(name="Test Product", description="This is a test product", price=9.99, stock=10)
        db.session.add(self.product)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_read_product(self):
        # Perform a GET request to read the product
        response = self.client.get(f'/products/{self.product.id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Product', response.data)
        self.assertIn(b'This is a test product', response.data)
        self.assertIn(b'9.99', response.data)
        self.assertIn(b'10', response.data)

if __name__ == '__main__':
    unittest.main()
