### Task 5: Optimize API Usage with Caching for Client Financial Data Retrieval

'''At AtliQ, you have been assigned to work on a new ad-hoc task for a client project involving a FINTECH company. Your task is to retrieve the company name based on the company's ticker. For example, for the ticker "AAPL", the company name will be "Apple Inc.". 

You are using the Bloomberg API for this, and each API call costs money. To reduce expenses, you want to implement a caching function using a decorator so that if a company name has previously been retrieved, it will be fetched from the cache; otherwise, an API call will be made. We don't have an actual API for this exercise, but we've provided you with a function called `get_company_name`, for which you can assume that every call incurs a cost, and your goal is to minimize the number of calls.

You will write a decorator,'''





'''tuple(...)
Converts the sorted list into a tuple: (('a', 1), ('b', 2)). Python dictionaries do not allow list or dict types as keys because they can be modified (unhashable), whereas a tuple is immutable (hashable) and works cleanly as a dictionary key.'''


def cache_decorator(func):
    cache = {}  # Stored outside wrapper so it persists across calls

    def wrapper(*args, **kwargs):
        # Create a key from the arguments passed to the function
        key = (args, tuple(sorted(kwargs.items())))

        if key in cache:
            return f"from cache: {cache[key]}"
        
        # Only run the function if the key is NOT in cache
        result = func(*args, **kwargs)
        cache[key] = result
        return f"from fetch: {result}"

    return wrapper

@cache_decorator
def get_company_name(ticker):

    api_responses = {
        "AAPL": "Apple Inc.",
        "MSFT": "Microsoft Corporation",
        "GOOGL": "Alphabet Inc."
    }
    return api_responses.get(ticker, "Unknown Company")


# Test the decorated function
print(get_company_name("AAPL"))  # Expected to trigger an API call
print(get_company_name("AAPL"))  # Expected to use cached data
print(get_company_name("MSFT"))  # Expected to trigger an API call
print(get_company_name("MSFT"))  # Expected to use cached data
print(get_company_name("GOOGL"))  # Expected to trigger an API call
print(get_company_name("GOOGL"))  # Expected to use cached data



