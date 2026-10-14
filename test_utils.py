import unittest

from utils import hello


class TestHello(unittest.TestCase):
    def test_hello_returns_greeting(self):
        self.assertEqual(hello(), 'Hello, Relay')

    def test_hello_return_type_is_str(self):
        self.assertIsInstance(hello(), str)


if __name__ == '__main__':
    unittest.main()
