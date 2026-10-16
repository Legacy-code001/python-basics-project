# We use Mocking to intercept the network call and return a pre-defined, fake response that we control.
# payment_gateway.py
import requests

def charge_payment_card(card_token, amount_cents):
    """Send a post request to the payment merchant API."""
    payload = {"token": card_token, "amount": amount_cents}
    response = requests.post("https://api.merchant.com/charge", json=payload)
    
    if response.status_code != 200:
        raise ConnectionError("Payment gateway declined transaction!")
    return response.json()


# test_payment_gateway.py
import pytest
from unittest.mock import patch, MagicMock
from payment_gateway import charge_payment_card

def test_charge_payment_card_success():
    """Test payment card charges with a mocked HTTP post response."""
    # Temporarily patch requests.post inside payment_gateway
    with patch("requests.post") as mock_post:
        # Create a simulated response object
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"id": "tx_90812", "status": "approved"}
        
        # Assign our simulated response to our mock post connector
        mock_post.return_value = mock_response
        
        # Execute the function
        result = charge_payment_card("tok_alice123", 450)
        
        # Verify the calculations
        assert result["id"] == "tx_90812"
        assert result["status"] == "approved"
        
        # Verify that the post was called with correct parameters
        mock_post.assert_called_once_with(
            "https://api.merchant.com/charge", 
            json={"token": "tok_alice123", "amount": 450}


# mock.patch.object
import pytest
from unittest.mock import patch
from my_service import PaymentProcessor

def test_payment_success():
    # Target the 'charge' method inside the PaymentProcessor class
    with patch.object(PaymentProcessor, 'charge', return_value=True) as mock_charge:
        processor = PaymentProcessor()
        result = processor.process_order(100)
        
        assert result is True
        mock_charge.assert_called_once_with(100)


# mock.patch.dict
import os
import pytest
from unittest.mock import patch

def test_development_mode_config():
    # Temporarily force an environment variable dictionary state
    test_env = {"APP_ENV": "development", "DEBUG": "True"}
    
    with patch.dict(os.environ, test_env, clear=True):
        # Inside this block, os.environ ONLY contains APP_ENV and DEBUG
        assert os.getenv("APP_ENV") == "development"
        
    # Outside the block, your computer's real os.environ is perfectly restored!
