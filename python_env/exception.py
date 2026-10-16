class IngredientShortageError(Exception):
    """Raised when a requested ingredient is out of stock in the inventory."""
    pass

class TemperatureSafetyError(Exception):
    """Raised when water temperature violates safe brewing parameters."""
    pass


class CoffeeKiosk:
    def __init__(self, beans_grams, temp_celsius):
        self.beans = beans_grams
        self.temp = temp_celsius

    def brew_coffee(self, cups):
        # 1. Validate safety rules
        if self.temp < 85.0 or self.temp > 98.0:
            raise TemperatureSafetyError(f"Dangerous brewing temperature: {self.temp}°C!")
        
        # 2. Validate ingredient stock
        beans_needed = cups * 18.0
        if self.beans < beans_needed:
            raise IngredientShortageError(f"Insufficient beans! Available: {self.beans}g.")
            
        self.beans -= beans_needed
        print(f"Successfully brewed {cups} cups of coffee!")
        return self.beans


        ''' TRY EXCEPT FINAL BLOCK'''
    try:
        print("Opening ingredient database file...")
        # Simulate reading a file
        raise FileNotFoundError("Missing inventory log!")
    except FileNotFoundError:
        print("Handling missing file... using defaults.")
    finally:
        # This ALWAYS runs, ensuring no memory leaks occur
        print("Closing database file and sanitizing system handles.")

        '''try, except, else block'''
        try:
            # Risky validation: parse user input
            quantity = int(input("How many espresso cups? "))
        except ValueError:
            print("Error: Invalid number format!")
        else:
            # Runs only if no ValueError occurred
            base_price = 3.50
            total = base_price * quantity
            print(f"Order validated! Total price: ₦{total:.2f}")

# In enterprise applications, failing to handle exceptions during file and database queries leads to leaked connections and locked resources:

try:
    connection = database.connect("coffee_cart_db")
    cursor = connection.cursor()
    cursor.execute("UPDATE inventory SET beans = 1000 WHERE id = 1")
except database.DatabaseError as e:
    print(f"Database write failed: {e}. Executing rollback...")
    connection.rollback()
finally:
    print("Closing database cursors safely.")
    cursor.close()
    connection.close()

# By placing connection.close() inside the finally block, we guarantee that no matter what went wrong during the SQL write, the database connection is closed safely, preserving server memory.zz


'''supressing chaining, hidden history'''

try:
    int("abc")
except ValueError:
    # Completely scrub the ValueError from the final crash traceback
    raise RuntimeError("Data processing failed") from None

'''standard chainning (explicit chainning)''''
try:
    # Attempting to open a missing configuration file
    with open("config.json", "r") as file:
        data = file.read()
except FileNotFoundError as error:
    # Raise a custom error, but link it to the root cause ('error')
    raise RuntimeError("Application failed to initialize") from error






BaseException
 ├── SystemExit (Raised when sys.exit() is called)
 ├── KeyboardInterrupt (Raised when user presses Ctrl+C)
 ├── GeneratorExit (Raised when a generator or coroutine is closed)
 └── Exception (The base class for all non-fatal/application errors)
      ├── ArithmeticError
      │    ├── FloatingPointError
      │    ├── OverflowError
      │    └── ZeroDivisionError (e.g., 1 / 0)
      ├── AssertionError (Raised when an 'assert' statement fails)
      ├── AttributeError (e.g., calling a method that doesn't exist)
      ├── BufferError
      ├── EOFError (End-of-file condition)
      ├── ImportError
      │    └── ModuleNotFoundError (e.g., import a missing library)
      ├── LookupError
      │    ├── IndexError (e.g., list index out of bounds)
      │    └── KeyError (e.g., dictionary key missing)
      ├── MemoryError
      ├── NameError (e.g., using a variable that wasn't defined)
      │    └── UnboundLocalError
      ├── OSError (System / File operations)
      │    ├── FileExistsError
      │    ├── FileNotFoundError (e.g., missing file path)
      │    ├── InterruptedError
      │    └── PermissionError (e.g., permission denied)
      ├── ReferenceError
      ├── RuntimeError (Generic catch-all error)
      │    └── NotImplementedError
      ├── SyntaxError (Invalid Python code structure)
      │    └── IndentationError
      │         └── TabError
      ├── TypeError (e.g., trying to add a string and an integer)
      └── ValueError (e.g., passing a valid type but invalid value)


