import unittest
from unittest.mock import patch, Mock

import weather.api as api


class TestGetWeather(unittest.TestCase):
    def test_success(self):
        sample = {
            "weather": [{"description": "clear sky", "icon": "01d"}],
            "main": {"temp": 23.5},
            "name": "Testville",
        }

        mock_resp = Mock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = sample

        mock_requests = Mock()
        mock_requests.get.return_value = mock_resp

        with patch("weather.api.requests", mock_requests):
            res = api.get_weather("Testville", api_key="key")
            self.assertEqual(res["city"], "Testville")
            self.assertEqual(res["temp"], 23.5)
            self.assertIn("description", res)

    def test_api_error(self):
        mock_resp = Mock()
        mock_resp.status_code = 404
        mock_resp.text = "Not found"

        mock_requests = Mock()
        mock_requests.get.return_value = mock_resp

        with patch("weather.api.requests", mock_requests):
            with self.assertRaises(ValueError):
                api.get_weather("NoCity", api_key="key")


if __name__ == "__main__":
    unittest.main()
