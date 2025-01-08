from Introduction import square
import pytest
def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
"""
pip install pytest
no main function needed , 
pytest takes cares of it
run program using pytest 4_Pytest.py 

"""
#We can segregate in categories as well
def positive_test():
    assert square(2) == 4
    assert square(3) == 9

def negative_test():
    assert square(-4) == 16
    assert square(-9) == 81

def zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):#testing if correct string is passed upon
        square("cat")
#Pytest will give results of each category differently