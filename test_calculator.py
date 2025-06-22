from calculator import add, subtract, multi, div

def test_add():
    assert add(2, 3) == 5
def test_add_basic():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-2, -3) == -5

def test_add_zero():
    assert add(0, 5) == 5

def test_subtract_basic():
    assert subtract(5, 3) == 2

def test_subtract_negative():
    assert subtract(-5, -2) == -3

def test_subtract_zero():
    assert subtract(0, 5) == -5
def test_multi_basic():
    assert multi(2,3)==6
def test_div_basic():
    assert div(6,3)==2
