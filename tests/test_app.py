import unittest
from app import create_app, db

class AppTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app('testing')
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()

    def test_home_page(self):
        response = self.app.test_client().get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Blog', response.data)

    def test_post_page(self):
        response = self.app.test_client().get('/post/1')
        self.assertEqual(response.status_code, 404)  # Assuming no posts exist yet

    def test_about_page(self):
        response = self.app.test_client().get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About Us', response.data)  # Assuming there's an about page

    def test_contact_page(self):
        response = self.app.test_client().get('/contact')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Contact Us', response.data)  # Assuming there's a contact page

if __name__ == '__main__':
    unittest.main()