import calculator

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(-1, -1) == -2

def test_subtract():
    assert calculator.subtract(2, 3) == -1
    assert calculator.subtract(-1, 1) == -2
    assert calculator.subtract(-1, -1) == 0

def test_multiply():
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(-1, 1) == -1
    assert calculator.multiply(-1, -1) == 1

def test_divide():
    assert calculator.divide(6, 3) == 2
    assert calculator.divide(-1, 1) == -1
    assert calculator.divide(-1, -1) == 1
    try:
        calculator.divide(1, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero!"
