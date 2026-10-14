import unittest

from utils import hello, slugify


class TestHello(unittest.TestCase):
    def test_hello_returns_greeting(self):
        self.assertEqual(hello(), 'Hello, Relay')

    def test_hello_return_type_is_str(self):
        self.assertIsInstance(hello(), str)


class TestSlugify(unittest.TestCase):
    def test_slugify_transliterates_accents(self):
        self.assertEqual(slugify('Crème Brûlée'), 'creme-brulee')


if __name__ == '__main__':
    unittest.main()
