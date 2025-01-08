from Introduction import square
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