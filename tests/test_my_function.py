import pytest
import source.my_function as myfunc

import time

def test_add():
    result = myfunc.add(1,4)
    assert result == 5

def test_add_strings():
    result = myfunc.add("i like ","burgers")
    assert result == "i like burgers"

def test_divide():
    result = myfunc.divide(10,5)
    assert result == 2

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        myfunc.divide(10,0)

def test_multiply():
    result = myfunc.multiply(6,5)
    assert result == 30

def test_remove():
    result = myfunc.remove(30,14)
    assert result == 16


@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = myfunc.divide(10,5)
    assert result == 2


@pytest.mark.skip(reason = 'This feature is broken')
def test_add():
    assert myfunc.add(1,2) == 3

@pytest.mark.xfail(reason = 'We know we cannot divide by zero')
def test_divide_zero_broken():
    myfunc.divide(10,0)