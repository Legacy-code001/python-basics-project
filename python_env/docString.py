def calculate_order_price(base_price, size, milk_surcharge=0.0):
    """Calculate the final transaction cost of a customized beverage order.
    
    This function computes the total price of a beverage after applying
    surcharges for large cup sizes and specialty alternative milks.

    Args:
        base_price (float): The baseline cost of the raw drink (e.g., 4.50).
        size (str): The requested cup size; must be "small", "medium", or "large".
        milk_surcharge (float, optional): Surcharge for alternative milk (e.g., 0.25). Defaults to 0.0.

    Returns:
        float: The final adjusted price of the beverage.

    Raises:
        ValueError: If base_price or milk_surcharge is negative.
        ValueError: If size is not one of the verified sizes.

    Examples:
        >>> calculate_order_price(4.50, "large", 0.25)
        5.25
        >>> calculate_order_price(-1.00, "small")
        ValueError: Prices cannot be negative!
    """
    if base_price < 0 or milk_surcharge < 0:
        raise ValueError("Prices cannot be negative!")
    
    size_multiplier = 1.0
    if size == "large":
        size_multiplier = 1.10
    elif size == "small":
        size_multiplier = 0.90
    elif size != "medium":
        raise ValueError(f"Invalid cup size: {size}")

    return (base_price * size_multiplier) + milk_surcharge




    """class docstrings"""
    '''The class docstring summarizes the object's role, lists its public attributes, and provides a quick instantiation example.'''


class SmartCup:
    """A standard coffee cup container that tracks liquid levels and cleanliness.
    
    This class represents a physical cardboard cup placed on the counter.
    It manages fill operations and prevents liquid overflow safety errors.

    Attributes:
        owner (str): The name of the customer who ordered the cup.
        capacity (float): The maximum liquid capacity of the cup in ounces.
        liquid_level (float): The current volume of liquid inside the cup.
        is_clean (bool): True if the cup is unused and clean, otherwise False.

    Examples:
        >>> cup = SmartCup("Alice", 12.0)
        >>> cup.fill(8.0)
        >>> cup.liquid_level
        8.0
    """

    def __init__(self, owner, capacity):
        """Initialize a new SmartCup object instance.

        Args:
            owner (str): The customer name to write on the side of the cup.
            capacity (float): The maximum liquid capacity in ounces (e.g., 12.0).
        """
        self.owner = owner
        self.capacity = capacity
        self.liquid_level = 0.0
        self.is_clean = True

    def fill(self, ounces):
        """Pour liquid into the cup, modifying its internal volume state.

        Args:
            ounces (float): The volume of liquid in ounces to pour inside.

        Raises:
            ValueError: If the poured ounces would exceed the cup's capacity.
        """
        if self.liquid_level + ounces > self.capacity:
            raise ValueError("Spill Warning: Poured volume exceeds cup capacity!")
        self.liquid_level += ounces
        self.is_clean = False

        """module"""
         kiosk_billing.py
        """kiosk_billing module containing functions to calculate totals and taxes.

        This module provides the primary financial algorithms for the automated
        coffee cart kiosk. It supports subtotal calculations, tax additions,
        discount applications, and formatted receipt exports.

        Examples:
        >>> from kiosk_billing import calculate_subtotal
        >>> calculate_subtotal(4.50, 3)
        13.5
        """

        import sys
        # Module code continues...

        """api enterprises quaity"""

        def charge_payment_card(card_token, amount_cents):
    """Charge a credit card securely via the payment gateway API.

    Args:
        card_token (str): The encrypted token representing the card.
        amount_cents (int): The transaction value in whole cents (e.g., 450 for ₦4.50).

    Returns:
        str: The transaction ID string if successful.

    Raises:
        ConnectionError: If the payment gateway cannot be reached.
        ValueError: If card_token is invalid or amount_cents is negative.
    """
    # API code here

    """doctest models"""
    def add_numbers(a, b):
    """
    Calculates the sum of two inputs.

    Examples:
    >>> add_numbers(2, 3)
    5
    >>> add_numbers(-1, 1)
    0
    >>> add_numbers(10.5, 0.5)
    
    11.0
    """
    return a + b

def divide_numbers(a, b):
    """
    Divides a by b. Handles division by zero gracefully.

    Examples:
    >>> divide_numbers(10, 2)
    5.0
    >>> divide_numbers(5, 0)
    Traceback (most recent call last):
    ZeroDivisionError: division by zero
    """
    return a / b

# This block allows you to run doctests directly from the terminal script
if __name__ == "__main__":
    import doctest
    doctest.testmod()



'''example involve writing the code with docstring not following any styling'''



class ShoppingCart:
    """
    A simple shopping cart that tracks items and prices.

    Example:
    >>> cart = ShoppingCart()
    >>> cart.add_item("Book", 12.99)
    >>> cart.add_item("Pen", 1.50)
    >>> cart.get_total()
    14.49
    """

    def __init__(self):
        self.items = {}

    def add_item(self, item_name, price):
        """
        Adds a single item to the cart. If the item exists, updates the price.

        >>> cart = ShoppingCart()
        >>> cart.add_item("Apple", 0.99)
        >>> "Apple" in cart.items
        True
        """
        self.items[item_name] = float(price)

    def remove_item(self, item_name):
        """
        Removes an item from the cart. Raises a KeyError if missing.

        >>> cart = ShoppingCart()
        >>> cart.add_item("Milk", 2.50)
        >>> cart.remove_item("Milk")
        >>> "Milk" in cart.items
        False
        >>> cart.remove_item("Missing Item")
        Traceback (most recent call last):
        KeyError: 'Missing Item'
        """
        if item_name not in self.items:
            raise KeyError(item_name)
        del self.items[item_name]

    def get_total(self):
        """Returns the total price of all items currently in the cart."""
        return sum(self.items.values())


# This block automatically executes the tests inside the docstrings when run directly
if __name__ == "__main__":
    import doctest
    # verbose=True forces it to print a detailed report even if everything passes
    doctest.testmod(verbose=True)




"""ANOTHER EXAMPLE"""
class ShoppingCart:
    """A simple shopping cart that tracks items and prices.

    Attributes:
        items (dict): A dictionary mapping item names (str) to prices (float).
    """

    def __init__(self):
        self.items = {}

    def add_item(self, item_name, price):
        """Adds a single item to the cart.

        If the item already exists, its price is overwritten.

        Args:
            item_name (str): The unique name of the item to add.
            price (float or int): The cost of the item.

        Raises:
            ValueError: If the price passed is a negative number.
            
        Examples:
            >>> cart = ShoppingCart()
            >>> cart.add_item("Apple", 0.99)
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.items[item_name] = float(price)

    def get_total(self):
        """Calculates the total price of all items currently in the cart.

        Returns:
            float: The sum total of all item prices.
        """
        return sum(self.items.values())
