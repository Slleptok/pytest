import pytest
import source.shapes as shape

@pytest.fixture
def  my_rectangle():
    return shape.Rectangle(10,20)

@pytest.fixture
def wierd_rectangle():
    return shape.Rectangle(5,6)