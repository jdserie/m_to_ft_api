import unittest

from m_to_ft import app


class ConverterTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_landing_page_and_conversion(self):
        self.assertEqual(self.client.get('/').status_code, 200)
        self.assertIn(b'1.000000 ft', self.client.get('/?meters=0.3048').data)

    def test_api_handles_signed_and_invalid_input(self):
        self.assertEqual(self.client.get('/api/convert?meters=-1').json, {
            'meters': '-1', 'feet': '-3.280840',
        })
        for raw in ('', 'NaN', '1e9', '1234567890123'):
            self.assertEqual(self.client.get('/api/convert', query_string={'meters': raw}).status_code, 400)

    def test_original_integer_endpoint(self):
        self.assertEqual(self.client.get('/meters/2').data, b'2 meters equals 6.56168 feet.')
