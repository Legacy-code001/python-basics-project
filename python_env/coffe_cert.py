# Coffee Cart with Static Typing, Google Style Docstrings, and Mock Tests

import unittest
from typing import Any, Dict, List, Optional, Tuple
from unittest.mock import patch, MagicMock
# =====================================================================# MODULE 1: cart.py (Core Shopping Cart Logic)# =====================================================================
class CoffeeCart:
    """Manages items added to a customer's coffee cart selection.

    Attributes:
        items (list): A list of dictionaries tracking added items. Each item 
            contains keys: 'name' (str), 'price' (float), and 'qty' (int).
        discount_code (float, optional): The decimal percentage multiplier for 
            active promotional discounts. Defaults to None.
    """

    # Static type annotations for class-level instance variables

    items: List[Dict[str, Any]]
    discount_code: Optional[float]

    def __init__(self) -> None:
        self.items = []
        self.discount_code = None

    def add_item(self, item: str, price: float, quantity: int = 1) -> None:
        """Adds a coffee item or beverage to the customer's selection.

        Args:
            item (str): The name of the beverage or product to add.
            price (float): The unit cost of the item.
            quantity (int, optional): The quantity of items to add. Defaults to 1.

        Raises:
            ValueError: If the quantity passed is less than or equal to zero.
        """
        if quantity <= 0:

            raise ValueError("Quantity must be positive")
        
        self.items.append({"name": item, "price": price, "qty": quantity})

    def apply_coupon(self, code: str) -> bool:
        """Validates and updates the cart's discount multiplier state.

        Args:
            code (str): The alphanumeric promotional code string.

        Returns:
            bool: True if the coupon code is valid and applied successfully, 
                False otherwise.
        """
        if code == "ESPRESSO10":
            self.discount_code = 0.10
            return True
        elif code == "BARISTA_PROMO":
            self.discount_code = 0.25

            return True
        return False

# =====================================================================# MODULE 2: pricing.py (Financial Computations Module)# =====================================================================
def calculate_totals(cart: CoffeeCart) -> Tuple[float, float, float]:
    """Calculates financial metrics for all items stored within a cart.

    Calculates subtotal sums, reduces the subtotal if active promotional 
    discount multipliers are detected, applies a standard 7.5% sales tax bounds, 
    and clips any negative totals to 0.00.

    Args:
        cart (CoffeeCart): An instance of the CoffeeCart class containing items.

    Returns:

        tuple: A tuple containing three elements rounded to 2 decimal places:
            - subtotal (float): Total cost after discounts are processed.
            - tax (float): Calculated sales tax amount (7.5%).
            - total (float): Final rounded absolute total cost.
    """
    subtotal: float = sum(item["price"] * item["qty"] for item in cart.items)
    
    if cart.discount_code:
        subtotal -= subtotal * cart.discount_code
        
    tax: float = subtotal * 0.075
    total: float = subtotal + tax
    
    if total < 0:
        return (0.00, 0.00, 0.00)   
        
    return round(subtotal, 2), round(tax, 2), round(total, 2)



# =====================================================================# MODULE 3: inventory.py (Stock Management Tracking)# =====================================================================
class CafeInventory:
    """Tracks and manages available ingredient stocks at the coffee station.

    Attributes:
        stock (dict): A dictionary mapping ingredient name strings (str) to 
            their available integer quantities (int).
    """

    # Static type annotation for internal stock tracker dictionary
    stock: Dict[str, int]

    def __init__(self) -> None:
        self.stock = {"Espresso": 100, "Milk": 50, "Syrup": 30}

    def check_and_reduce(self, item: str) -> bool:

        """Verifies if an ingredient item is in stock and decrements it.

        Args:
            item (str): The name of the ingredient item to check.

        Returns:
            bool: True if the item is in stock and successfully decremented, 
                False otherwise.
        """
        if self.stock.get(item, 0) > 0:
            self.stock[item] -= 1
            return True
        return False

# =====================================================================# AUTOMATED TEST SUITE WITH MOCK ASSERTIONS# =====================================================================

class TestCoffeeCartSystem(unittest.TestCase):
    """Executes validation scripts matching the baseline coverage paths."""

    def test_cart_initialization(self) -> None:
        """Verifies that new coffee cart instances spawn with pristine empty states."""
        cart = CoffeeCart()
        self.assertEqual(len(cart.items), 0)
        self.assertIsNone(cart.discount_code)

    def test_add_valid_item(self) -> None:
        """Verifies standard item entry registration mechanics."""
        cart = CoffeeCart()
        cart.add_item("Latte", 4.50, 2)
        self.assertEqual(len(cart.items), 1)
        self.assertEqual(cart.items[0]["name"], "Latte")
        self.assertEqual(cart.items[0]["qty"], 2)

    def test_apply_coupon_espresso(self) -> None:
        """Tests the tracking path for the baseline ESPRESSO10 promotion option."""

        cart = CoffeeCart()
        success = cart.apply_coupon("ESPRESSO10")
        self.assertTrue(success)
        self.assertEqual(cart.discount_code, 0.10)

    def test_apply_invalid_coupon(self) -> None:
        """Verifies fallback operations when handling a nonsense code string input."""
        cart = CoffeeCart()
        success = cart.apply_coupon("FAKE_CODE")
        self.assertFalse(success)
        self.assertIsNone(cart.discount_code)

    def test_pricing_calculations_with_discount(self) -> None:
        """Validates accuracy for subtotal, sales tax, and final rounded totals."""
        cart = CoffeeCart()
        cart.add_item("Espresso", 3.00, 2)
        cart.apply_coupon("ESPRESSO10")
        
        subtotal, tax, total = calculate_totals(cart)

        
        self.assertEqual(subtotal, 5.40)
        self.assertEqual(tax, 0.41)      
        self.assertEqual(total, 5.81)    

    def test_inventory_stock_reduction(self) -> None:
        """Tracks complete code line validation paths across inventory managers."""
        inv = CafeInventory()
        self.assertTrue(inv.check_and_reduce("Espresso"))
        self.assertEqual(inv.stock["Espresso"], 99)
        self.assertFalse(inv.check_and_reduce("Chai_Tea"))

    # -----------------------------------------------------------------
    # MOCK ASSERTION TESTS WITH TYPE HINTS
    # -----------------------------------------------------------------

    def test_apply_coupon_with_patch_object(self) -> None:
        """Demonstrates patch.object mock assertions on an object instance."""
        cart = CoffeeCart()

        
        with patch.object(cart, 'apply_coupon', return_value=True) as mock_coupon:
            result = cart.apply_coupon("HOLIDAY50")
            
            self.assertTrue(result)
            mock_coupon.assert_called_once()
            mock_coupon.assert_called_once_with("HOLIDAY50")

    @patch('__main__.calculate_totals')
    def test_checkout_pipeline_with_decorator_patch(self, mock_calc_totals: MagicMock) -> None:
        """Demonstrates standalone function mocking via a patch decorator hook."""
        mock_calc_totals.return_value = (20.00, 1.50, 21.50)
        
        fake_cart = CoffeeCart()
        fake_cart.add_item("Cold Brew", 5.00, 4)
        
        subtotal, tax, total = calculate_totals(fake_cart)
        
        self.assertEqual(subtotal, 20.00)

        self.assertEqual(total, 21.50)
        
        mock_calc_totals.assert_called_with(fake_cart)
        self.assertEqual(mock_calc_totals.call_count, 1)

if __name__ == "__main__":
    print("🚀 Initiating Coffee Cart Suite Test Sequence...\n")
    unittest.main(exit=False)


