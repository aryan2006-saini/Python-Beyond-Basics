import pytest
import source.my_functions as my_functions
import time

def test_add():
    result = my_functions.add(1,4)

    # assert is used for debugging a statement
    assert result==5


def test_add_strings():
    result = my_functions.add("i like ", "burgers")
    assert result=="i like burgers"

def test_divide():
    result = my_functions.divide(4,2)

    assert result==2

def test_divide_by_zero():
    # with pytest.raises(ZeroDivisionError): #error because we are returning value error in the main function
    
    with pytest.raises(ValueError):
        my_functions.divide(10,0)

# mocking and parametrization

#this test is going to be slow one
@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = my_functions.divide(10, 5)
    assert result==2

@pytest.mark.skip(reason="This feature is currently broken")
def test_add():
    assert my_functions.add(1,2)==3


@pytest.mark.xfail(reason="we know we can't divide by zero")
def test_divide_zero_broken():
    my_functions.divide(4,0)