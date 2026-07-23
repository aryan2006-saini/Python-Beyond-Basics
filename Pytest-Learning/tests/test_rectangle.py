import pytest
import source.shapes as shapes

# we have initialized the rectangle two time, we can fix this using @pytest.fixture
# def test_area():
#     rectangle = shapes.Rectangle(10, 20)

#     assert rectangle.area()==10*20


# def test_perimeter():
#     rectangle = shapes.Rectangle(10, 20)

#     assert rectangle.perimeter()==2*(10+20)

# we can even make this global using configtest.py
    # @pytest.fixture
    # def my_rectangle():
    #     return shapes.Rectangle(10,20)

    # @pytest.fixture
    # def weird_rectangle():
    #     return shapes.Rectangle(5,6)


def test_area(my_rectangle):
    assert my_rectangle.area()==10*20

def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter()==2*(10+20)

def test_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle
