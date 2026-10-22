import pytest
from unittest.mock import patch
from src.search import check_api

def test_successful_request():
    with patch("src.search.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "message": "Success"
        }

        result = check_api("https://example.com")

        assert result == {"message": "Success"}
        mock_get.assert_called_once_with(
            "https://example.com", timeout=10
        )




def test_failed_request():
    with patch("src.search.requests.get") as mock_get:
        mock_get.return_value.status_code = 404

        with pytest.raises(ValueError, match="API request failed"):
            check_api("https://example.com")

        mock_get.assert_called_once_with(
            "https://example.com", timeout=10
        )