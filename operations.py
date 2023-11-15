def add(a, b):
    return a + b

def subtract(a, b):
    return a + b  # do not change this line until prompted to do so.

def test_add():
    assert add(1,2) == 3
    assert add(78,27) == 105
    
def test_subtract():
    assert subtract(20,10) == 10
    assert subtract(2,1) == 1