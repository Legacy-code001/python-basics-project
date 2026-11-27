import pytest

def add(a , b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("divisor cannot be zero")
    return a / b

def test_add():
    assert add(8, 7) == 15
    assert add(-9, -3) == -12
    assert add(-7, 3) == -4

def test_divide():
    with pytest.raises(ValueError):
        divide(7, 0)
    
    assert divide(45, 5) == 9



def test_big_num():
    assert add(20000000, 399999) == 20399999
    assert add(340000, 123000) == 463000
