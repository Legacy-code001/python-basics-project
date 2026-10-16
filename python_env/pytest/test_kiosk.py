# test_kiosk.py
import pytest
from kiosk import CoffeeKiosk

@pytest.fixture
def stocked_kiosk():
    """Provide a pre-configured kiosk containing ingredients."""
    # Setup: create and return the object
    return CoffeeKiosk(beans_grams=100.0, water_ml=500.0)

def test_brew_espresso_consumes_inventory(stocked_kiosk):
    # Action: brew a cup using our fixture object
    stocked_kiosk.brew_espresso()
    
    # Assert: verify inventory was deducted correctly
    assert stocked_kiosk.beans == 82.0
    assert stocked_kiosk.water == 470.0

def test_insufficient_ingredients_raises_error(stocked_kiosk):
    # Deplete the kiosk inventory
    stocked_kiosk.beans = 10.0
    
    # Assert: verify exception is raised
    with pytest.raises(ValueError):
        stocked_kiosk.brew_espresso()