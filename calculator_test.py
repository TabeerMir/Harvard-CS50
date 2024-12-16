from calculator import square
import pytest
'''def main():
    test_square()

def test_square():
    try :
        assert square(2) ==4
    except AssertionError:
        print ('2 squared wasnt 4')
    try:
        assert square(3)== 9
    except AssertionError:
        print('3 squared wasnt 9')
    try:
        assert square(-2)== 4
    except AssertionError:
        print('-2 squared wasnt 4')
    try:
        assert square(-3)== 9
    except AssertionError:
        print('-3 squared wasnt 9')
    try:
        assert square(0)== 0
    except AssertionError:
        print('0 squared wasnt 0')

if __name__ == '__main__':
    main()'''

def test_positive():
    assert square (2) == 4
    assert square(3)==9

def test_negative():    
    assert square (-2) ==4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_string():
    with pytest.raises(TypeError):
        square('cat')