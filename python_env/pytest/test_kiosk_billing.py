# test_kiosk_billing.py
import pytest
from kiosk_billing import calculate_subtotal, apply_discount

def test_calculate_subtotal_success():
    """Verify that multiplying prices by quantities returns the correct total."""
    result = calculate_subtotal(4.50, 3)
    assert result == 13.50

def test_calculate_subtotal_negative_raises_error():
    """Verify that negative inputs trigger a ValueError."""
    with pytest.raises(ValueError):
        calculate_subtotal(-4.50, 3)

def test_apply_discount():
    """Verify that discounts are deducted correctly."""
    result = apply_discount(10.00, 0.10)
    assert result == 9.00


# test_kiosk_billing.py
import pytest
from kiosk_billing import calculate_subtotal

@pytest.mark.parametrize("price, quantity, expected", [
    (4.50, 2, 9.00),
    (3.50, 3, 10.50),
    (5.00, 0, 0.00),
    (0.00, 5, 0.00),
])
def test_calculate_subtotal_parametrized(price, quantity, expected):
    assert calculate_subtotal(price, quantity) == expected